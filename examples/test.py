from specter import Specter

screen = Specter()

def popup():
  screen.popup(["This is a", "multiline popup"])

def example2(p):
  screen.splash(p)

def example():
  screen.splash([{'t': 'This is an example :)'}])

def justified():
  someText = ["This is a very long line. So long, it shouldn't fit on most screens. You should consider yourself lucky if this fits on a single screen. I'm coding this on a small laptop, so for me it doesn't fit",
              {'t': "This is the second line of text", 'm': "bold"}]
  to_print = screen._justify(someText)
  screen.splash(to_print)

def userinput():
  inp = screen.userInput("Type some text")
  screen.splash([inp])

longString = '''This is a very long line. So long, it shouldn't fit on most screens. You should consider yourself lucky if this fits on a single screen.'''

text = [{'t': "this is a test", 'm':'bold'}]
splash = [{'t': 'random splash screen', 'm': 'title'},
          {'t': 'random text filling the screen'},
          {'t': ' '},
          {'t': '  [ Press enter to continue ]', 'm': 'bold'}]
table = [{'tn': 'table1', 'tc': [{'t': "Head1", 'm': 'title'},   "Head2",   "Head3",  "Head4"]},
         {'tn': 'table1', 'tc': ["val1",    "val2",    "val3",   "val 4" ]},
         {'tn': 'table1', 'tc': ["value1",  "value__2",  "value3", "value4" ]}]
text.extend(table)

for i in range(1, 11):
  text.extend([{'t': "line "+ str(i)}])
text.extend([{'t': longString}])
text.extend([{'t': 'Press e or u for examples of functions bound to keys'}])
text.extend([{'t': 'Press Enter here to perform a function with args', 'a': example2, 'p': ["Some text"]}])
text.extend([{'t': 'Press Enter here to show text in a justified splash screen', 'a': justified}])

screen.start()
screen.splash(splash)
screen.scroll(text, functions={'e': example, 'u': userinput, 'p': popup}, cursor=True)
screen.stop()
