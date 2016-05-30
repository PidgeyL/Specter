import curses
import copy
import sys
import traceback

from . import Defaults as defaults
from .specterbase import SpecterBase
from .Debugger import Debugger

def cursWrapped(func):
  def curs_wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except KeyboardInterrupt:
      curses.endwin()
      sys.exit("KeyboardInterrupt: Exiting gracefully")
    except:
      curses.endwin()
      sys.exit(traceback.print_exc())
  return curs_wrapper

class Specter(SpecterBase):
  @cursWrapped
  def splash(self, text, border=True):
    try:
      self.screen.clear()
      if border: self.screen.border(1)
      maxy,maxx=self.screen.getmaxyx()
      if len(text)>maxy:
        text=text[:maxy-2] # Shorten text if window too small
      textlength = max([self._getLen(x) for x in text])
      if textlength < maxx - 4: # 4 represents a border of 2 on each side
        start = int((maxx/2)-(textlength/2))
      else:
        start = 2
      # Print the splash text
      for i, line in enumerate(text): self._print(i+1, start, line)
      self.screen.refresh()
      self.screen.getch()
    except Exception as e:
      self.stop()
      raise(e)

  @cursWrapped
  def scroll(self, text,header=[],footer=[],cursor=False,blocking=True,nav={}, functions={}):
    try:
      # Default Values
      contInd=0
      cursInd=0
      cursPos=0
      sideInd=0
      sideMax=max([self._getLen(x) for x in text]) if text else 0
      b=self.border

      # Extend the navigation
      navSet = copy.deepcopy(defaults.navSet) # Copy default settings
      userNav= copy.deepcopy(nav)
      for dKey in userNav.keys(): # Add all the custom keys
        if dKey not in navSet.keys(): navSet[dKey]=[] # Ensure it exists
        for val in nav[dKey]: # Add all values that match the type
          if   type(val) is int: navSet[dKey].append(val)
          elif type(val) is str: navSet[dKey].append(ord(val))

      # Set cursor position if given (and int)
      if type(cursor)==int:
        maxy,maxx=self.screen.getmaxyx()
        maxCont=maxy-len(header)-len(footer)-4
        cursInd=cursor if cursor < len(text) else len(text)
        if len(text)-cursInd>maxy or cursInd < maxCont or len(text)-1<maxy:
          # everything fits on the screen
          # calculate cursor pos from the beginning
          cursPos=cursor if cursor < maxCont-1 else maxCont-1
          # no need to scroll down yet
          contInd=0 if cursor < maxCont else len(text)-1-cursInd+maxCont
        elif len(text)-cursInd<maxCont:
          # we have to scroll the cursor up starting from the end
          cursPos=maxCont-(len(text)-cursInd)
          # fit the last part of the screen
          contInd=len(text)-maxCont
        else:
          # cursor at the bottom
          cursPos=maxCont-1
          # scroll to corresponding index
          contInd=cursInd-maxCont+1
        cursor=True

      # Start Display-loop
      while True:
        # Get the maximum content size
        maxy,maxx=self.screen.getmaxyx()
        maxCont=maxy-len(header)-len(footer)-4
        s=len(header)+2 if len(header)!=0 else 1
        self.screen.clear()
        lines = copy.deepcopy(text)
        # Make a list of the tables for printing
        self._generateTables(lines, sideInd)
        # Take only the content that fits on the screen
        # Y-axis
        if len(text)>maxCont: lines=lines[contInd:contInd+maxCont]
        #X-axis
        for line in lines: self._cutText(line, sideInd, maxx+sideInd-b)

        # Print the content to the screen
        #  - Header
        for i,line in enumerate(header):
          self._print(i+1, b, line, self.getMarkup('header'))
        #  - Content
        for i,line in enumerate(lines):
          self._print(i+s, b, line)
        # Set cursor if needed
        if cursor:
          self._print(cursPos+s,1,">")
        #  - Footer
        for i,line in enumerate(footer):
          self._print((maxy-len(footer)-1)+i,b,line, self.getMarkup('footer'))

        # Wait for the user to make a move
        key=self.screen.getch()
        if key in navSet['up']:
          if cursor:
            if cursInd>0:cursInd-=1
            if cursPos==0 and contInd>0:contInd-=1
            if cursPos>0:cursPos-=1
          else:
            if contInd>0:contInd-=1
        elif key in navSet['down']:
          if cursor:
            if cursInd<len(text)-1:cursInd+=1
            if cursPos==maxCont-1 and (len(text)-contInd)>maxCont:contInd+=1
            if cursPos<maxCont-1 and cursPos<len(text)-1:cursPos+=1
          else:
            if (len(text)-contInd)>maxCont:contInd+=1
        elif key in navSet['left']:
          if sideInd > 0: sideInd-=1
        elif key in navSet['right']:
          if sideInd + maxx -b*2< sideMax: sideInd+=1
        elif key in navSet['home']:
          sideInd = 0
        elif key in navSet['end']:
          sideInd = sideMax - maxx - b*2
        elif key in navSet['next']:
          if sideInd + maxx - b*2 <= sideMax - maxx - b*2:
            sideInd = sideInd + maxx - b*2
          else:
            sideInd = sideMax - maxx + b*2
        elif key in navSet['prev']:
          if sideInd - maxx + b*2 >= 0:
            sideInd = sideInd - maxx + b*2
          else:
            sideInd = 0
        elif key in navSet['pg_up']:
          if contInd - maxCont >= 0: contInd-=maxCont
          else: contInd = 0
        elif key in navSet['pg_dn']:
          if contInd + maxCont < len(text):contInd+=maxCont
          else: contInd = len(text)-maxCont
        elif key in navSet['esc']:
          return chr(key) if blocking else (chr(key),cursInd)
        elif key in navSet['enter'] and cursor:
          if 'a' in text[cursInd]: # There is an action
            if 'p' in text[cursInd]:
              text[cursInd]['a'](text[cursInd]['p'])
            else:
              text[cursInd]['a']()
        else:
          if chr(key) in functions.keys():
            functions[chr(key)]()
          elif not blocking:
            return (chr(key),cursInd)

    except Exception as e:
      self.stop()
      raise(e)


  def userInput(self, text):
    x, y = self.getMaxXY()
    newScreen=curses.newwin(4, x, y-5, 0)
    newScreen.erase()
    newScreen.box()
    self._print(1,2,text, dest=newScreen)
    self._print(2,3,">", dest=newScreen)
    curses.echo()
    line=newScreen.getstr(2,5).strip().lower()
    line=str(line,'utf-8')
    curses.noecho()
    newPanel=curses.panel.new_panel(newScreen)
    newPanel.top()
    curses.panel.update_panels()
    self.screen.refresh()
    return line

  def popup(self, text):
    length = max([self._getLen(x) for x in text])
    x, y = self.getMaxXY()
    lines = copy.deepcopy(text)
    for line in lines: self._cutText(line, 0, x-2)
    winX = min(x-2, length+4)
    winY = min(x-2, len(lines)+2)
    posX = int((x-winX)/2)
    posY = int((y-winY)/2)
    newScreen=curses.newwin(winY, winX, posY, posX)
    newScreen.erase()
    newScreen.box()
    for i,line in enumerate(lines):
      self._print(i+1, 2, line, dest=newScreen)
    newScreen.getch()
    newPanel=curses.panel.new_panel(newScreen)
    newPanel.top()
    curses.panel.update_panels()
    self.screen.refresh()
