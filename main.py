import kivy

kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
	def build(self):
		return Label(text = 'This is the first app')


if(__name__ == '__main__'):
	MyApp().run()
