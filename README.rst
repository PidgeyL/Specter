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
    screen.start()
    screen.scrollDisplay(text)
    screen.stop()

Authors
=======

Pieter-Jan Moreels / `@pidgeyl <http://github.com/pidgeyl>`__
