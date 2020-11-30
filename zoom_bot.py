import datetime
import time
import keyboard
import os
from selenium import webdriver
class zoom_bot:
	def join(self,meeting_link):
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.bot.get(meeting_link)
		time.sleep(3)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(10)

		self.bot.quit()

link1 = open("meeting_link1.txt","r").read()
link2 = open("meeting_link2.txt","r").read()

obj = zoom_bot()
obj.join(link1)

time.sleep(3000)

obj = zoom_bot()
obj.join(link2)

time.sleep(3000)

