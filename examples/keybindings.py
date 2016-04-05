import curses

try:
  scr=curses.initscr()
  curses.noecho()
  curses.curs_set(0)
  Continue = True
  x = False
  while Continue:
    scr.clear()
    if x:
      scr.addstr(3,1," -> ordinal value:  %s"%x)
      scr.addstr(4,1," -> str of ordinal: %s"%chr(x))
    scr.addstr(0,1,"Press a button and we'll give you it's ordinal value")
    scr.addstr(1,1,"Press q to quit")
    x = scr.getch()
    if x == ord("q"):
      scr.addstr(5,1,"  -> You pressed q. Do you want to quit? (y/n)")
      x = scr.getch()
      if x == ord("y"):
        Continue = False
  curses.endwin()
except Exception as e:
  curses.endwin()
  print(e)
