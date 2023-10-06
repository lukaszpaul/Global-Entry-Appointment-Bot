Global Entry Appointment Bot
This bot checks for available Global Entry interview appointment slots at JFK airport and alerts you when an opening is found.

Usage
The script checks the CBP appointment API every 5 seconds for available slots at the JFK location (locationId=5140). When an opening is found, it prints the available time(s) and plays an alert sound.

To use it:

Clone the repo
Install dependencies (requests)
Run python bot.py
The location can be changed by modifying the locationId parameter in the API URL.

Requirements
Python 3
Requests module
Mac OS (for alert sound)
Customization
Change the location ID to check other centers
Modify the alert sound or add other notifications like email/SMS
Adjust the check interval by changing the sleep timer
Disclaimer
This bot is meant for personal use to monitor appointment availability. Please use responsibly. Overloading the booking system may have negative impacts.

Let me know if you would like me to modify or expand the README further!
