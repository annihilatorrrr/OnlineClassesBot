# Online Classes Bot 

OnlineClassesBot is a Python Program which attends your Zoom Online Classes.

## Requirements

* Chrome/Chromium WebBrowser 
* Zoom Meeting App
* Python 3.x
* pip3
 
## Installation & Usage

On Windows:
-
> Download ChromeDriver from here 'https://chromedriver.chromium.org/downloads'
 
 Download this repository and extract the contents.
 Open Command Prompt and run the follow commands:

`cd path/to/extracted/contents/`

`python -m pip install -r requirements.txt`

`Uncomment Line 8 in 'zoom_bot.py'`

 The Bot is ready to work now,
 Put the invite links of your online classes and delay between them in 'config.py'.
 Run the following commands to run the bot:

`cd path\to\the\folder\where\you\extracted\the\contents`

`python zoom_bot.py`

On Linux:

`Download the .zip from 'https://chromedriver.chromium.org/downloads' according to your Chrome/Chromium Version`

`unzip chromedriver_linux64.zip`

`mv chromedriver_linux64/* /usr/lib/chromium-browser/`

`Uncomment Line 9 in 'zoom_bot.py'`

`git clone https://github.com/Kody-K/OnlineClassesBot/`

`cd OnlineClassesBot`

`python3 -m pip install -r requirements.txt`

 The Bot is ready to work now,
 Put the invite links of your online classes and delay between those classes in 'config.py'.
 Run the following commands (in the same directory) to run the bot:
 
`python zoom_bot.py`
