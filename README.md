# OnlineClassesBot
My simple Python Program which automates the process of joining classes.

How does it work?

It all goes like this:
1. You Double-Click on the zoom_bot.py file and walk away or if you are curious you sit back and see everything happening. 
2. The program reads the 'meeting_link1.txt' file in the 'meeting_links' folder. 
3. The 'meeting_link1.txt' file contains the invite link for the first online class, which is opened by Chrome Browser as per the instructions given by the program.
4. The keyboard library comes into action and allows the zoom popup to launch zoom.
5. Zoom launches and joins the meeting.
6. The program sleeps for 50 mins. (I have 1 class of 40 mins and then a short-break of 10 mins).
7. After 50 mins, the 'zoom_bot.py' wakes up and brings his friend 'zoom_bot2.py' into action.
8. The 'zoom_bot2.py' grabs the invite link of 2nd Class and joins it in the same way as the 'zoom_bot.py' did.

Installations:

Windows:
1. Download the zip file and extract it.
2. Make sure that you have python installed on your PC.
3. Double Click on setup.py to setup everything.
4. Delete all previously added text from the 'meeting_link1.txt' and 'meeting_link2.txt' and put the invite links of your classes respectively.
5. Double Click on zoom_bot.py and walk away.

Linux:

1. Make sure that you have python and pip installed on your PC.
2. Launch your terminal and run the following commands:
* git clone https://Kody-K/OnlineClassesBot/ 
* cd OnlineClassesBot
* python setup.py
* python zoom_bot.py
Walk Away and let the Bot do its work.
