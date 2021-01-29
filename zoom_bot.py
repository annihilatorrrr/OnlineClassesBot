import time
import keyboard
from selenium import webdriver
from config import delay, meeting_links as links

class zoom_bot:
	def join_meeting(self,link):
#		self.bot = webdriver.Chrome("chromedriver.exe")
#		self.bot = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
		self.bot.get(link)
		time.sleep(5)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(10)
		self.bot.quit()

bot = zoom_bot()
for link in links:
    bot.join_meeting(link)
    if delay > 1:
        time.sleep(delay)
