# -*- coding: UTF-8 -*-

"""
    specter
    ~~~~~~

    Curses Framework for Python

    :copyright: (c) 2016 by Moreels Pieter-Jan.
    :license: BSD, see LICENSE for more details.
"""

from .specter import Specter
from .shell import SpecterShell
from .Debugger import Debugger

import curses

KEY_RIGHT = curses.KEY_RIGHT
KEY_LEFT  = curses.KEY_LEFT
KEY_UP    = curses.KEY_UP
KEY_DOWN  = curses.KEY_DOWN
KEY_ESC   = 27
KEY_ENTER = 10

__copyright__ = 'Copyright 2016 by Moreels Pieter-Jan'
__version__ = '0.2.1'
__license__ = 'BSD'
__author__ = 'Moreels Pieter-Jan'
__email__ = 'pieterjan.moreels@gmail.com'
__source__ = 'https://github.com/pidgeyl/pidgeyl'

