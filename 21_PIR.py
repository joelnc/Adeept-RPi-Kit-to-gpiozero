

from gpiozero import MotionSensor, LED
from subprocess import call
from signal import pause

# Set pin for motion sensor
pir = MotionSensor(4) # as in pin 7

# Define function to play sound file
def play_click():
        call(["aplay", "-i",
              "/home/jen/camera-shutter-click-02.wav"])

# When motion is detected, run the play_click function
pir.when_motion = play_click
        
pause()
