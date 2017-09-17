#! /usr/bin/python3

#This is a comment here, to test GIT
import time
import datetime
import shelve
import os
import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class TrainGridLayout(GridLayout):
	pass

class TrainApp(App):
	def build(self):
		return TrainGridLayout()

trApp=TrainApp()
trApp.run()