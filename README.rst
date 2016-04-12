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

Authors
=======

Pieter-Jan Moreels / `@pidgeyl <http://github.com/pidgeyl>`__
