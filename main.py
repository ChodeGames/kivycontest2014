from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.animation import Animation

class Butt(Button):
	def clicked(self):
		print "The button that was clicked has a center of "+str(self.center)
		x, y = self.center
		playersizex, playersizey = self.parent.player1.size
		print "The current player size is "+str(self.parent.player1.size)
		self.parent.player1.move((x-(playersizex/2), y-(playersizey/2)))

class BGTCGame(FloatLayout):
	player1 = ObjectProperty(None)
	'''
	#all the buttons, is this necessary?
	upper_left = ObjectProperty(None)
	upper_midleft = ObjectProperty(None)
	upper_center = ObjectProperty(None)
	upper_midright = ObjectProperty(None)
	upper_right = ObjectProperty(None)
	midupper_left = ObjectProperty(None)
	midupper_right = ObjectProperty(None)
	midlower_left = ObjectProperty(None)
	midlower_right = ObjectProperty(None)
	lower_left = ObjectProperty(None)
	lower_midleft = ObjectProperty(None)
	lower_center = ObjectProperty(None)
	lower_midright = ObjectProperty(None)
	lower_right = ObjectProperty(None)
	'''

class Player(Widget):
	def move(self, newpos):
		print "New position for player is "+str(newpos)
		print "Player size is "+str(self.size)
		animation = Animation(pos=newpos)
		animation.start(self)

class BGTCApp(App):
	def build(self):
		game = BGTCGame()
		return game

if __name__ == '__main__':
	BGTCApp().run()


