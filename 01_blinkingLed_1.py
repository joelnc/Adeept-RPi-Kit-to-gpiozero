#-----------------------------------------------------------
# File name   : 01_blinkingLed_1.py
# Description : Make an led blink. This script differs in that
#               it uses .on and .off instead of .blink in the
#               previous script. Goes to show, there's more than
#               one way to skin a cat....

#-----------------------------------------------------------

# Import LED and pause functions only... not the entire libraries
from gpiozero import LED
from time import sleep

# Set the control pin to match the wiring setup.
# This can be an identical setup to the previous script.
myLed = LED(17) # pin 11/GPIO17

# Set a new variable 'blinkLight' to True
blinkLight = True

# As long as blinkLight is True, run the following commands
# over and over again
while blinkLight == True:
        myLed.on() # turn on led
        sleep(1)   # sleep/do nothin for x seconds
        myLed.off()# turn off led
        sleep(1)   # sleep again, timing in seconds

# That's it! No need to pause() script at the end because it will
# keep running as long as blinkLight is set True, and we never set
# it to false.
