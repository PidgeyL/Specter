from specter import Specter

screen = Specter()
longString = '''This is a very long line. So long, it shouldn't fit on most screens. You should consider yourself lucky if this fits on a single screen.'''

text = [{'t': "this is a test", 'm':'bold'}]
splash = [{'t': 'random splash screen', 'm': 'title'},
          {'t': 'random text filling the screen'},
          {'t': ' '},
          {'t': '  [ Press enter to continue ]', 'm': 'bold'}]
for i in range(1, 11):
  text.extend([{'t': "line "+ str(i)}])
text.extend([{'t': longString}])
text.extend([{'t': 'Press e or u for examples of functions bound to keys'}])

def example():
  screen.splash([{'t': 'This is an example :)'}])

def userinput():
  inp = screen.userInput("Type some text")
  screen.splash(inp)

screen.start()
screen.splash(splash)
screen.scroll(text, functions={'e': example, 'u': userinput})
screen.stop()
