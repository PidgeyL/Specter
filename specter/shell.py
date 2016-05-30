import curses
import copy
import sys
import _thread
import traceback

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

class SpecterShell(SpecterBase):
  def __init__(self, backend, markupSet={}):
    super().__init__(markupSet, border=0)
    self.backlog = []
    self.backend = backend

  def writeln(self, line):
    self.backlog.append(line)
  def delete(self, lines):
    self.backlog = self.backlog[:-lines]
  @cursWrapped
  def refresh(self):
    self.screen.clear()
    to_print = self._justify(self.backlog)
    X, Y = self.getMaxXY()
    for y, line in enumerate(to_print[-Y+2:]):
      self._print(y, 0, line)
    self.screen.refresh()

  @cursWrapped
  def listen(self):
    try:
       _thread.start_new_thread(self._listen, ())
    except KeyboardInterrupt:
      self.running = False
      t=None

  def _shellPrompt(self, cursor=">"):
    try:
      x, y = self.getMaxXY()
      newScreen=curses.newwin(1, x, y-2, 0)
      newScreen.erase()
      self._print(0,1,cursor, dest=newScreen)
      curses.echo()
      line=newScreen.getstr(0,len(cursor)+2).strip().lower()
      line=str(line,'utf-8')
      curses.noecho()
      newPanel=curses.panel.new_panel(newScreen)
      newPanel.top()
      curses.panel.update_panels()
      self.screen.refresh()
      return line
    except:
      return ""

  def _listen(self):
    self.running = True
    while self.running:
      message = self._shellPrompt()
      self.backend.userinput(message)
    self.running = False

  def _listen_(self):
    self.running = True
    while self.running:
      try:
        message = self._shellPrompt()
      except EOFError:
        break
      except KeyboardInterrupt:
        break
      self.backend.userinput(message)
    self.running = False
