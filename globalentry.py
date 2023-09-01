import requests
import json
import time
import os
import subprocess

def play_sound():
    try:
        subprocess.call(["afplay", "/System/Library/Sounds/Ping.aiff"])
    except Exception:
        pass

def check_available_slots():
    url = "https://ttp.cbp.dhs.gov/schedulerapi/slot-availability?locationId=5140"
    count = 1  

    while True:
        try:
            response = requests.get(url)
            data = response.json()

            if len(data["availableSlots"]) > 0:
                print(f"{count}. Available Slot(s):")
                for slot in data["availableSlots"]:
                    times = slot['startTimestamp']
                    print(times)
                play_sound()
            else:
                print(f"{count}. None")


        except Exception as e:
            print(f"Error: {e}")
 
        count += 1  
        time.sleep(5)

if __name__ == "__main__":
    play_sound()
    check_available_slots()
