from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard
import os
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

link = open("meeting_link1.txt","r").read()

obj = zoom_bot()
obj.join(link)

time.sleep(3000)

os.system("cd Desktop/Kode/bot/")
os.system("python zoom_bot2.py")
