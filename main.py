from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class BGTCGame(FloatLayout):
	pass

class BGTCApp(App):
	def build(self):
		game = BGTCGame()
		return game

if __name__ == '__main__':
	BGTCApp().run()


