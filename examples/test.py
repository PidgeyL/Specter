from specter import Specter

screen = Specter()
text = [{'t': "this is a test", 'm':'bold'}]
splash = [{'t': 'random splash screen', 'm': 'title'},
          {'t': 'random text filling the screen'},
          {'t': ' '},
          {'t': '  [ Press enter to continue ]', 'm': 'bold'}]
for i in range(1, 11):
  text.extend([{'t': "line "+ str(i)}])
screen.start()
screen.splash(splash)
screen.scroll(text)
screen.stop()
