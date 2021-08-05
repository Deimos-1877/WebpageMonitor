# WebpageMonitor
A program to check for changes to a webpage and send an alert when the webpage changes.

Be sure to have the following python packages installed (use pip install ...): bs4; yagmail; PyQt5

Execute the file WebpageMonitor.py to start the program.
A graphical user interface should appear, asking for input.


The program requires the following input:

A webpage to monitor. 
    This should be entered with http:// or https:// at the beginning of the URL to function properly.
  
An Email/Emails to alert.
    The program will send an email alert to the entered email, once the webpage changes. Enter one email, or enter multiple emails seperated by a comma (no spaces)
  
An Email to send the alert from.
    This must be a GMAIL account. Enter only the username (everything before @gmail.com). 
    Less secure access must be enabled in the security settings of the account. It is recommended to create a new account for this.
  
The password to the email to send the alert from.
    The password to the GMAIL account.
  
Delay time.
    The delay time between consecutive checks. Enter this as an intiger, seconds. Please remember that quick checks may be mistaken for a Denial Of Service Attack.
  
Start and Stop time.
    Select True if you would like the program to check the website for changes only during specific times of the day. Otherwise select false.
  
Start time.
    If you have selected True for the Start and Stop time option, enter a intiger start time in the 24 hour format (e.g. 7 for 7am and 19 for 7pm). Otherwise leave empty.
  
Stop time
    If you have selected True for the Start and Stop time option, enter a intiger stop time in the 24 hour format. Otherwise leave empty.
  
With LED for raspberry Pi.
    If you are running this program on a raspberry Pi, you can connect an LED to confirm that the program is running. Select True for this option and connect and LED to GPIO pin 17. Select False otherwise.
  
Press Start Monitor to start the program. Confirmation of the program running and working should be seen in the Console.

Troubleshooting.
    Should you continuously see "Error checking website" in the console, please check your internet connection. Also check if you have correclty entered the webpage and other options.
    No email alerts: please check that you have correctly entered the email to alert, the username of the alert sending gmail account and its password. Please also check that your Gmail security settings.   
