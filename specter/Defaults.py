import curses

mkset = {'normal': ('white', 'black', False),
         'bold':   ('white', 'black', True),
         'header': ('red',   'black', True), 
         'footer': ('red',   'black', True),
         'title':  ('blue',  'black', True)}

cursColors = {'red':    curses.COLOR_RED,
              'white':  curses.COLOR_WHITE,
              'black':  curses.COLOR_BLACK,
              'green':  curses.COLOR_GREEN,
              'yellow': curses.COLOR_YELLOW,
              'blue':   curses.COLOR_BLUE}

KEY_ESC = 27   # Curses Value of the ESC key (And ALT)
KEY_ENTER = 10 # Curses Value of the Enter key

navSet = {'up':    [curses.KEY_UP],
          'down':  [curses.KEY_DOWN],
          'left':  [curses.KEY_LEFT],
          'right': [curses.KEY_RIGHT],
          'esc':   [KEY_ESC],
          'enter': [KEY_ENTER],
          'home':  [],
          'end':   [],
          'next':  [],
          'prev':  [],
          'pg_up': [],
          'pg_dn': []}
