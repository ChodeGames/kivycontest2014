from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.animation import Animation

class Butt(Button):
	button_index = NumericProperty(1)
	def clicked(self):
		print "The button that was clicked has a center of "+str(self.center)
		#x, y = self.center
		#playersizex, playersizey = self.parent.player1.size
		print "The current player size is "+str(self.parent.player1.size)
		print "The location_list is:"
		print self.parent.location_list
		#self.parent.player1.move((x-(playersizex/2), y-(playersizey/2)))
		self.parent.player1.move(self.button_index)

class BGTCGame(FloatLayout):
	player1 = ObjectProperty(None)
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
	location_list = []
	'''
	location_list numbering scheme looks like this:
	0	1	2	3	4
	13				5
	12				6
	11	10	9	8	7
	'''
	def set_list(self):
		print "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
		print self.upper_left
		self.location_list = [self.upper_left, self.upper_midleft,
						self.upper_center, self.upper_midright, self.upper_right,
						self.midupper_left, self.midupper_right, self.midlower_left, self.midlower_right,
						self.lower_left, self.lower_midleft,
						self.lower_center, self.lower_midright, self.lower_right
						]
		print self.upper_left
	
	

class Player(Widget):
	location_index = NumericProperty(2)
	'''
	def move(self, newpos):
		print "New position for player is "+str(newpos)
		print "Player size is "+str(self.size)
		animation = Animation(pos=newpos)
		animation.start(self)
	'''
	def move(self, target_button_index):
		#find out how far away we are from that button if we go clockwise
		direction = 'clockwise'
		distance = 0
		if target_button_index > self.location_index:
			distance += (len(self.parent.location_list) - target_button_index)
			distance += self.location_index
		
		#if it's too far to go clockwise, then go counter-clockwise
		if distance > (len(self.parent.location_list) / 2):
			direction = 'counterclockwise'
			distance = (len(self.parent.location_list) - distance)
		
		#make a list buttons in the correct order
		button_list = []
		if direction == 'clockwise':
			if self.location_index + distance > len(self.parent.location_list):
				button_list = self.parent.location_list[self.location_index:]
				button_list += self.parent.location_list[:target_button_index]
			else:
				button_list = self.parent.location_list[self.location_index:target_button_index]
		elif direction == 'counterclockwise':
			if self.location_index - distance < 0:
				button_list = self.parent.location_list[self.location_index::-1]
				button_list += self.parent.location_list[
					len(self.parent.location_list):target_button_index:-1
				]
			else:
				button_list = self.parent.location_list[self.location_index:target_button_index:-1]
		
		print "button_list is"
		print button_list
		
		#make the animation and run it
		animation = Animation()
		for button in button_list:
			animation += Animation(
							pos=(
								button.center[0]-(self.size[0]/2),
								button.center[1]-(self.size[1]/2)
							)
						)
		animation.start(self)
		
		#set the players location_index so we know where he is
		self.location_index = target_button_index

class BGTCApp(App):
	def build(self):
		game = BGTCGame()
		game.set_list()
		print "==HEY=="
		print game.location_list
		print game.upper_left
		return game

if __name__ == '__main__':
	BGTCApp().run()


