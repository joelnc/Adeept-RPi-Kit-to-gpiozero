#-----------------------------------------------------------
# File name   : 01_blinkingLed_0.py
# Description : Make an led blink using a python scirpt to conrol
#               the gpio pins.
#
# Don't forget your safety glasses :)
#-----------------------------------------------------------

# Import LED and pause functions only... not the entire libraries
from gpiozero import LED
from signal import pause

# Set the control pin to match the wiring setup.
# This builds off of ../01_led.png
myLed = LED(17) # pin 11 / GPIO17

# Set the LED to blink where the input number defines how long on/off
myLed.blink(.5) # in units of seconds

# Without this call to "Signal pause" the LED will blink once
# and the then the script is over.  This call makes it keep running
# until it is manually killed at the shell 
pause()

# That's it.  Compare the 3 lines of code in this script to the code
# in Orig_Files/01_blinkingLed_1.py.  Much easier.

