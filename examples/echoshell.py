from specter import SpecterShell


class Backend():
  def __init__(self):
    self.gui = SpecterShell(self)
    self.gui.listen()

  def userinput(self, message):
    self.gui.writeln("You wrote: %s"%message)
    self.gui.refresh()

shell = Backend()
try:
  while True:
    pass
except KeyboardInterrupt:
  shell.gui.stop()
