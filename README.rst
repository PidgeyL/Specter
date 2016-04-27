======
Specter
======

Specter is a curses framework for Python. It implements curses and makes certain aspects a lot easier. <br />
Currently supported:
 * Scrollable text
 * Markup for every line of text

Installation
============

Simple:

.. code-block:: console

    $ sudo python3 setup.py install
    or
    $ sudo python setup.py install

Example
=======

.. code-block:: console

    import specter
    text = [{'t': "This could be a header", 'm':'bold'},
            {'t': "This could be normal text"}]
    screen=specter.Specter()
    screen.start()
    screen.scrollDisplay(text)
    screen.stop()

Classes & Functions
===================

 * **Specter(markupSet=None, border=2)**
   * start()                 - *start curses in specter*
   * stop()                  - *gracefully stop specter*
   * getBorder()             - *returns width of borders*
   * setBorder(border)       - *sets width of borders*
     * *border* **int** - amount of columns left and right
   * getMarkupSet()          - *returns the current markup set*
   * setMarkupSet(markupSet) - *sets the preferred markupset*
     * *markupSet* **dict** - prefered markup set
   * getMaxXY()              - *returns the X and Y coordinates tupel*
   * splash(text[, border])  - *makes a splashscreen*
     * *text* **list**   - text to display on splash screen
     * *border* **bool** - enable frame around the splash screen
   * scroll(text[, header][, footer][, cursor][, blocking][, nav][,functions]) - *displays lines of text and allows scrolling*
     * *text* **list**   - text to display on scroll screen
     * *header* **list** - text to display on top of the scroll screen
     * *footer* **list** - text to display on bottom of the scroll screen
     * *cursor* **bool** - enable the cursor
     * *blocking* **bool** - don't do anything if a key not in nav is pressed. Includes default nav
     * *nav*    **dict** - dictionary of keys linked to actions
     * *functions* **dict** - list of functions bound to keys
   * userInput(text)     - *asks the user for input*
     * *text* **str** - text above the user input
 * **Debugger**
   * send(data [,addr][,port]) - *send messages containing any data (mind space limit). Default: 127.0.0.1:5055*
   * listen([addr][,port])     - *listen to messages sent. Default: 127.0.0.1:5055*

Variables
=========
text
----

The text variable is a list of lines to display. The format of these lines are very flexible. 
The lines in the text variable can exist of either strings or dictionaries.
Strings are very straightforward: the string represents the text to be shown.
Dictionaries are more flexible. There are several keys that can be used:

 * **t**  - *text*        - The text to display
 * **m**  - *markdown*    - The markdown to use. Use the key of the loaded markdown of choice
 * **a**  - *action*      - A pointer of the function to bind to the line
 * **tn** - *table name*  - The name of the table to bind the cells to. These allow to differentiate tables
 * **tc** - *table cells* - A list of cells of a table. Each cell has to conform to the same format

Some rules have to be followed though.

 * tc and tn always have to come together. If not, the line will be ignored.
 * if tc, tn and t are in the same line, only t will be used
 * m is only applicable on t, not on tc's

markdown
--------

The markdown variable is a dictionary, where each key is a markdown type. These can be overwritten.
The value of each key is a tuple of 3, where the first is the text color, the second is the background color
 and the third is a boolean, representing "Bold". Below is the default markdown:

.. code-block:: console
    {'normal': ('white', 'black', False),
     'bold':   ('white', 'black', True),
     'header': ('red',   'black', True),
     'footer': ('red',   'black', True),
     'title':  ('blue',  'black', True)}

navigation set
--------------
The navigation set variable is a dictionary, where each key is a navigation.
This cannot be overwritten, but can be extended.
home, end, next, prev, pg_up and pg_dn are left empty, and can be customized.

The values for the navset can be either a char or an int. For more information,
 use ./examples/keybindings.py to find either the ordinal value or the char representing
the key.

Below is the default navset

.. code-block:: console

    {'up':    [curses.KEY_UP],
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


Authors
=======

Pieter-Jan Moreels / `@pidgeyl <http://github.com/pidgeyl>`__
