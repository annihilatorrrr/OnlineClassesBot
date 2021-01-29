import time
import keyboard
import os
from selenium import webdriver

class zoom_bot:
    def join_meeting(self,link):
        try:
            if os.name == 'posix':
                self.bot = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
            else:
                self.bot = webdriver.Chrome("chromedriver.exe")
            self.bot.get(link)
            time.sleep(5)
            keyboard.send("tab", do_press=True, do_release=True)
            keyboard.send("tab", do_press=True, do_release=True)
            keyboard.send("enter", do_press=True, do_release=True)
            time.sleep(10)
            self.bot.quit()
        except Exception as e:
            print(str(e))

run_mode = int(input(" Choose A Running Mode:\n 1. Terminal\n 2. Telegram Bot\n > "))
bot = zoom_bot()


if run_mode == 1:
    from config import delay, meeting_links as links
    for link in links:
        bot.join_meeting(link)
        if delay > 1:
            time.sleep(delay)
elif run_mode == 2:
    from pyrogram import Client, filters
    from config import bot_token, owner_id
    app = Client(':memory:',
            bot_token=bot_token,
            api_id=6,
            api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")


    @app.on_message(filters.command('start'))
    def start(_, message):
        message.reply_text("Hi, I'm Zoom Bot, Send Help To Get Commands.")


    @app.on_message(filters.command('help'))
    def help(_, message):
        message.reply_text("/join <<link>> - To Join A Meeting")


    @app.on_message(filters.command('join') & filters.user(owner_id))
    def joinbot(_, message):
        if len(message.command) != 2:
            message.reply_text("/join Requires A Meeting Link As Argument.")
            return

        if message.entities[1]['type'] != 'url':
            message.reply_text("/join Requires A Meeting Link As Argument.")
            return
        
        link = message.command[1]
        m = message.reply_text("Joined Meeting.")
        try:
            bot.join_meeting(link)
        except Exception as e:
            m.edit(str(e))
            print(str(e))

    app.run()
else:
    print("No Input, detected, Exiting!")
