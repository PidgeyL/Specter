from specter import Specter

screen = Specter()
text = [{'t': "this is a test", 'm':'bold'}]
for i in range(1, 11):
  text.extend([{'t': "line "+ str(i)}])
screen.start()
screen.scrollDisplay(text, nav={'esc': ['q']})
screen.stop()
