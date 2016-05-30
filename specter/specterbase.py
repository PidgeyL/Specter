import math
import copy
import curses, curses.panel

from . import Defaults as defaults
from .Exceptions import MarkupException

class SpecterBase():
  def __init__(self, markupSet={}, border=2):
    self.screen = None
    try:
      self.border=border
      self.start()
      self.setMarkupSet(markupSet)
      self.tables={}
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


  def getBorder(self):
    return self.border

  def setBorder(self, border):
    if type(border) == int:
      self.border = border
      return True
    else:
      return False

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
        colorID+=1
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

  def getMaxXY(self):
    y, x = self.screen.getmaxyx()
    return (x, y) # Personally I like X, Y better for math reasons

  def _print(self, y, x, line, markdown=None, dest=None):
    if not dest: dest = self.screen
    if type(line) == str: line = {'t': line} # Transform to dict
    if type(line) == dict: # Valid line to print
      if type(markdown) == str: line['m']=markdown # Apply markdown

      if 'm' in line:
        markup = self.getMarkup(line['m'])
      else:
        markup = self.getMarkup('normal')

      if 't' in line:
        dest.addstr(y,x,str(line['t']),markup)
      elif 'tn' in line and 'tc' in line:
        for i, cell in enumerate(line['tc']):
          offset=sum(self.tables[line['tn']][:i])
          self._print(y, x+offset, cell)
      else:
        dest.addstr(y,x,"Line is an invalid format")

  def _justify(self, text, border=None):
    if border is None:
      border = self.border
    data = []
    X, Y = self.getMaxXY()
    X = X - (2*border) # Remove borders
    # Chop up the backlog to make it print-able
    for line in copy.deepcopy(text):
      length = self._getLen(line)
      for i in range(math.ceil(length/X)):
        data.append(self._cutText(line, i*X, i*X+X))
    return data

  def _getLen(self, text):
    if type(text) is not dict and type(text) is not str: text = str(text)
    if type(text) == dict and 't' in text: text=text['t']
    if type(text) == str: return len(text)
    else: return 0

  def _cutText(self, text, start, end):
    if type(text) == dict:
      if 't' in text: text['t']=text['t'][start:end]
      elif 'tc' in text and 'tn' in text:
        for i, cell in enumerate(self.tables[text['tn']]):
          if cell is 0:
            text['tc'][i]=""
          else:
            start -= sum(self.tablesOrig[text['tn']][:i])
            text['tc'][i] = self._cutText(text['tc'][i], start, end)
            break
    elif type(text) == str: text=text[start:end]
    return text

  def _generateTables(self, lines, offset, border = 1):
    self.tables={}
    # Check for tables. tn for tablename and tc for tablecells
    for line in lines:
      if type(line) is dict and 'tn' in line and 'tc' in line:
        if line['tn'] in self.tables:
          multiplier = (len(self.tables[line['tn']])-len(line['tc']))
          self.tables[line['tn']].extend([0]*multiplier)
          for i, cell in enumerate(line['tc']):
            width=max(self.tables[line['tn']][i], self._getLen(cell))
            self.tables[line['tn']][i]=width+border
        else: self.tables[line['tn']]=[len(x)+border for x in line['tc']]
    self.tablesOrig = copy.deepcopy(self.tables)

    lastTN=""
    for line in lines:
      if (type(line) is dict and 'tn' in line and 'tc' in line and
         lastTN != line['tn']):
        lastTN = line['tn']
        for i, cell in enumerate(line['tc']):
          if self.tables[line['tn']][i] <= offset:
            offset -= self.tables[line['tn']][i]
            self.tables[line['tn']][i]=0
          elif offset is not 0:
            self.tables[line['tn']][i]-=offset
            offset=0



