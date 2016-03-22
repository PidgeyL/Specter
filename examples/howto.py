from specter import Specter

screen = Specter()
df = ['Press ENTER to select', 'Press ESC to quit'] # Default footer


def mainPage():
  h=['Main Page']
  t=[{'t': "Overview Functions", 'a': functions},
     {'t': "Markdown",           'a': markdownExample}]
  screen.scroll(t, header=h, footer=df, cursor=True)

def functions():
  h=['Overview Functions']
  t=[{'t': "scroll", 'm': 'title'},
     {'t': "======", 'm': 'title'},
     {'t': "'scroll' is able to scroll through large texts, in different modes."},
     {'t': "The parameters of the function are explained below:"},
     {'t': " * text    - Required - A list of dictionaries representing the content."},
     {'t': "    -> Press Enter here to see an example", 'm': 'bold', 'a': textExample},
     {'t': " * header  - Optional - A list of strings, representing a header."},
     {'t': " * footer  - Optional - A list of strings, representing a footer."},
     {'t': " * cursor  - default False - Change to cursor mode."},
     {'t': "      Cursor mode allows the user to select a line and trigger functions"},
     {'t': "      that are assigned to that line."},
     {'t': " * blocking - default True - Blocks the user from entering any other keys"},
     {'t': "      that are not the ESC or the up/down/left/right nav keys"},
     {'t': "   -> NOTE: left and right currently not supported", 'm': 'bold'},
     {'t': " * nav     - Optional - A dictionary with default nav keys as keys"},
     {'t': "      allows to extend the default nav keys (up/down/left/right/enter/esc)"},
     {'t': "   -> Press Entr here to see an more information and examples"},
     {'t': " "},
     {'t': "INFO: This page is made using scroll, with cursor=True", 'm': 'bold'}]
  screen.scroll(t, header=h, footer=df, cursor=True)

def textExample():
  h=['Example text format']
  t=[{'t': "In this section we'll explain the format of the text parameter"},
     {'t': "We'll start with an example, and explain the different parts"},
     {'t': " "},
     {'t': "l=[{'t': 'This is a title of my paragraph', 'm': 'title'}"},
     {'t': "   {'t': 'This is the first line of my paragraph'}"},
     {'t': "   {'t': 'Below, we have a list I made'}"},
     {'t': "   {'t': ' * item 1'}"},
     {'t': "   {'t': ' * item 2'}"},
     {'t': "   {'t': ' * item 3'}"},
     {'t': "   {'t': 'Here, we can trigger our function', 'a': myFunct}]"},
     {'t': " "},
     {'t': "We made a variable 'l' which is the list of text we want to display"},
     {'t': "  t -> the text we want to display (t for text)"},
     {'t': "  m -> the type of colors and attributes we want to apply (m for markdown)"},
     {'t': "        (Look in 'Main Page > Markdown' for more information and examples)"},
     {'t': "  a -> the function we want to execute on hitting enter (a for action)"},
     {'t': "        (Later on, we will also support strings containing code)"},
     {'t': " "},
     {'t': "INFO: This page is made using scroll, with cursor=False", 'm': 'bold'}]
  screen.scroll(t, header=h, footer=df)

def markdownExample():
  h=['Example Markdown']
  t=[{'t': "In this section we'll explain the format of the markdown variable"},
     {'t': "We'll start with an example, and explain the different parts"},
     {'t': " "},
     {'t': "m={'normal': ('white', 'black', False)"},
     {'t': "   'bold':   ('white', 'black', True)"},
     {'t': "   'header': ('red',   'black', True)"},
     {'t': "   'footer': ('red',   'black', True)"},
     {'t': "   'title':  ('blue',  'black', True)}"},
     {'t': " "},
     {'t': "We made a variable 'm' which is a dictionary containing keys with the name"},
     {'t': "of the markdown."},
     {'t': "The value contains a tupel with a length of three."},
     {'t': " - The first tupel value is the foreground color"},
     {'t': " - The second tupel value is the background color"},
     {'t': " - The third tupel value is a boolean. True means bold text, False is normal"},
     {'t': " "},
     {'t': "The current supported colors are: 'red', 'white', 'black', 'green', 'yellow'"},
     {'t': "and 'blue'"},
     {'t': " "},
     {'t': "The markdown example (m) is the default color palet. You can modify the current"},
     {'t': "colors or add your own markdown. This is explained in the next section"},
     {'t': " "},
     {'t': "Setting and reading the markdown", 'm': 'title'},
     {'t': "================================", 'm': 'title'},
     {'t': "Adding a markdown can be done either at the initiation of the specter object,"},
     {'t': "or afterwards, using the 'setMarkupSet' function."},
     {'t': "The current markup set can be requested by using the function"},
     {'t': "'getMarkupSet'."},
     {'t': "Information about a certain markup can be requested by using"},
     {'t': "'getMarkup'. This function takes a string with the title of the"},
     {'t': "markdown"},
     {'t': " ! The values of the first two tupel values are integers."},
     {'t': " "},
     {'t': "INFO: This page is made using scroll, with cursor=False", 'm': 'bold'}]
  screen.scroll(t, header=h, footer=df)


mainPage()
screen.stop()
