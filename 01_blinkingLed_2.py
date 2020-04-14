#-----------------------------------------------------------
# File name   : 01_blinkingLed_2.py
# Description : Make an led blink. This script adds a function
#               'toggleTF' that changes the value of blinkLed.
#               Later we will control the LED using a button but
#               this shows how we can use Python to expand control
#               of the LED using functions.

#-----------------------------------------------------------

# Import LED and pause functions only... not the entire libraries
from gpiozero import LED
from time import sleep

# Set the control pin to match the wiring setup.
# This can be an identical setup to the previous script.
myLed = LED(17) # pin 11/GPIO17

# Set a new variable 'blinkLight' to True
global blinkLight
blinkLight = True

# Function to chnage blinkLight from T to F, then back to T
def toggleTF():
        global blinkLight
        blinkLight = False
        sleep(6)
        blinkLight = True
        # not working as expected.. this fun keeps light on rather
        # than turning it off....?

# As long as blinkLight is True, run the following commands
# over and over again
while blinkLight == True:
        myLed.on() # turn on led
        sleep(2)   # sleep/do nothin for x seconds
        myLed.off()# turn off led
        sleep(.5)   # sleep again, timing in seconds
        myLed.on() # turn on led
        sleep(2)   # sleep/do nothin for x seconds
        myLed.off()# turn off led
        sleep(.5)   # sleep again, timing in seconds
        toggleTF()
        
# In the previous script the LED keeps blinking since blinkLight is
# permanently stuck on 'True'.  Here the value changes to 'False' when
# the 'toggleTF' function gets called.  
