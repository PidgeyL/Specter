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
    self.cursor = ">"

  def writeln(self, line):
    self.backlog.append(line)
  def delete(self, lines):
    self.backlog = self.backlog[:-lines]
  @cursWrapped
  def refresh(self):
    if not self.screen: return
    self.screen.clear()
    to_print = self._justify(self.backlog)
    X, Y = self.getMaxXY()
    for y, line in enumerate(to_print[-Y+2:]):
      self._print(y, 0, line)
    # redraw the cursor
    self._print(Y-1,1,self.cursor)
    self.screen.refresh()

  def _shellPrompt(self):
    try:
      X, Y = self.getMaxXY()
      curses.echo()
      self._print(Y-1,1,self.cursor)
      line=self.screen.getstr(Y-1,len(self.cursor)+2).strip().lower()
      line=str(line,'utf-8')
      curses.noecho()
      self.refresh()
      return line
    except:
      return ""

  @cursWrapped
  def listen(self):
    try:
       _thread.start_new_thread(self._listen, ())
    except KeyboardInterrupt:
      self.running = False
      t=None

  def _listen(self):
    self.running = True
    while self.running:
      message = self._shellPrompt()
      self.backend.userinput(message)
    self.running = False

  def stop(self):
    self.running=False
    super().stop()
