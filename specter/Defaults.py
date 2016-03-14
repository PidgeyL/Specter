import curses

mkset = {'normal': ('white', 'black', False),
         'bold':   ('white', 'black', True),
         'header': ('red',   'black', True), 
         'footer': ('red',   'black', True)}

cursColors = {'red':    curses.COLOR_RED,
              'white':  curses.COLOR_WHITE,
              'black':  curses.COLOR_BLACK,
              'green':  curses.COLOR_GREEN,
              'yellow': curses.COLOR_YELLOW,
              'blue':   curses.COLOR_BLUE}
