
import pyautogui
import random
import time
import datetime
import screeninfo
import time
import sys


def move_mouse(x, y,time):
    pyautogui.moveTo(x, y,time,pyautogui.easeInQuad)

def get_screen_center():
    screen = screeninfo.get_monitors()[0]
    center_x = screen.x + screen.width // 2
    center_y = screen.y + screen.height // 2
    return center_x, center_y

center_x, center_y = get_screen_center()

#x_pos = center_x
#y_pos = center_y
x_max,y_max = pyautogui.size()


duration = 60  # Default duration
sleepTime = 0.1 # Default interval
diameter = 333 # Default diameter

# Get duration from command line arguments
if "-duration" in sys.argv:
    duration_index = sys.argv.index("-duration")
    if duration_index + 1 < len(sys.argv):
        duration = int(sys.argv[duration_index + 1])

# Get interval (miliseconds) from command line arguments
if "-interval" in sys.argv:
    interval_index = sys.argv.index("-interval")
    if interval_index + 1 < len(sys.argv):
        interval = int(sys.argv[interval_index + 1])
        sleepTime = interval / 1000 


print("SleepTime:", sleepTime)  
print("Duration:", duration)    

# Calculate the end time of the loop
end_time = datetime.datetime.now() + datetime.timedelta(minutes=duration)
pyautogui.PAUSE = 0.01

while datetime.datetime.now() < end_time:
    # Generate random positions

    x_pos, y_pos = pyautogui.position()

    x_pos += random.randint(-diameter, diameter)
    y_pos += random.randint(-diameter, diameter)
    
    if x_pos > x_max:
        x_pos = x_max
    elif x_pos < 0:
        x_pos = 0
    if y_pos > y_max:
        y_pos = y_max
    elif y_pos < 0:
        y_pos = 0

    print("Moving mouse to:",x_pos,y_pos)
    # Move the mouse to random position
    move_mouse(x_pos, y_pos,sleepTime)
    time.sleep(sleepTime-0.01)
