from specter import Specter

screen = Specter()
df = ['Press ENTER to select', 'Press ESC to quit'] # Default footer


def mainPage():
  h=['Main Page']
  # We use g as a placeholder (goto) to know which function to trigger
  t=[{'t': "Overview Functions", 'a': functions}]
  screen.scrollDisplay(t, header=h, footer=df, cursor=True)

def functions():
  h=['Overview Functions']
  t=[{'t': "scrollDisplay", 'm': 'title'},
     {'t': "=============", 'm': 'title'},
     {'t': "scrollDisplay is able to scroll through large texts, in different modes."},
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
     {'t': "INFO: This page is made using scrollDisplay, with cursor=True", 'm': 'bold'}]
  screen.scrollDisplay(t, header=h, footer=df, cursor=True)

def textExample():
  h=['Example text format']
  t=[{'t': "In this section we'll explain the format of the text parameter"},
     {'t': "We'll start with an example, and explain the different parts"},
     {'t': " "},
     {'t': "t=[{'t': 'This is a title of my paragraph', 'm': 'title'}"},
     {'t': "   {'t': 'This is the first line of my paragraph'}"},
     {'t': "   {'t': 'Below, we have a list I made'}"},
     {'t': "   {'t': ' * item 1'}"},
     {'t': "   {'t': ' * item 2'}"},
     {'t': "   {'t': ' * item 3'}"},
     {'t': "   {'t': 'Here, we can trigger our function', 'a': myFunct}]"},
     {'t': " "},
     {'t': "We made a variable 't' which is the text we want to display"},
     {'t': "  t -> the text we want to display (t for text)"},
     {'t': "  m -> the type of colors and attributes we want to apply (m for markdown)"},
     {'t': "        (Look in 'Main Page > Markdown' for more information and examples)"},
     {'t': "  a -> the function we want to execute on hitting enter (a for action)"},
     {'t': "        (Later on, we will also support strings containing code)"},
     {'t': " "},
     {'t': "INFO: This page is made using scrollDisplay, with cursor=False", 'm': 'bold'}]
  screen.scrollDisplay(t, header=h, footer=df)


mainPage()
screen.stop()
