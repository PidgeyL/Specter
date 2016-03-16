import copy
import curses

from . import Defaults as defaults
from .Exceptions import MarkupException

class Specter():
  def __init__(self, markupSet={}):
    self.screen = None
    try:
      self.start()
      self.setMarkupSet(markupSet)
    except Exception as e:
      self.stop()
      raise(e)

  def start(self):
    try:
      # Start curses
      self.screen=curses.initscr()
      curses.start_color()  # Enable Colors
      curses.curs_set(0)    # Set Cursor to Top
      curses.noecho()       # Don't show cursor
      self.screen.keypad(1) # Enable keypad
    except Exception as e:
      self.stop()
      raise(e)

  def stop(self):
    try:
      curses.endwin()
      self.screen = None
    except Exception as e:
      print(e)

  def getMarkupSet(self):
    return self.markup

  def setMarkupSet(self, markupSet):
    self.markup = {}                    # Purging the current markupset
    markSet = copy.copy(defaults.mkset) # Copy default settings
    markSet.update(markupSet)           # Overwrite user settings
    colorID=1
    try:
      co = defaults.cursColors # Shorten var name to reduce code size
      for mk in markSet.keys():
        if type(mk) == str:
          mset = markSet[mk] # Shorten var name to reduce code size
          curses.init_pair(colorID, co[mset[0]], co[mset[1]])
          if mset[2]:
            self.markup[mk]=curses.color_pair(colorID) | curses.A_BOLD
          else:
            self.markup[mk]=curses.color_pair(colorID)
    except Exception as e:
      print(e)
      raise(MarkupException)

  def getMarkup(self, key):
    try:
      return self.markup[key]
    except:
      print("Tried markup '%s'"%key)
      print("The current markup set contained:")
      print(self.markup)
      raise(MarkupException)

  def scrollDisplay(self, text,header=[],footer=[],cursor=False,blocking=True,nav={}):
    try:
      # Default Values
      contInd=0
      cursInd=0
      cursPos=0

      # Extend the navigation
      navSet = copy.copy(defaults.navSet) # Copy default settings
      for dKey in nav.keys(): # Add all the custom keys
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
        lines=list(text)
        # Take only the content that fits on the screen
        if len(text)>maxCont:
          lines=lines[contInd:contInd+maxCont]
        # Print the content to the screen
        #  - Header
        for i,line in enumerate(header):
          self.screen.addstr(i+1,2,line, self.getMarkup('header'))
        #  - Content
        for i,line in enumerate(lines):
          if 'm' in line:
            markup = self.getMarkup(line['m'])
          else:
            markup = self.getMarkup('normal')
          if 't' in line:
            self.screen.addstr(i+s,2,line['t'],markup)
          # Temporarily removed key/val format
          else:
            self.screen.addstr(i+s,2,"Line is an invalid format")
        # Set cursor if needed
        if cursor:
          self.screen.addstr(cursPos+s,1,">")
        #  - Footer
        for i,line in enumerate(footer):
          self.screen.addstr((maxy-len(footer)-1)+i,2,line)

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
        elif key in navSet['esc']:
          return chr(key) if blocking else (chr(key),cursInd)
        elif key in navSet['enter'] and cursor:
          if 'a' in text[cursInd]: # There is an action
            text[cursInd]['a']()
        else:
          if not blocking:
            return (chr(key),cursInd)
    except Exception as e:
      self.stop()
      raise(e)
