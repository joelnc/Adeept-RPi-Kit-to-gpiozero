#-----------------------------------------------------------
# File name   : 02_buttonLed_0.py
# Description : Turn LED on/off via button press.
# Wiring      : See gpiozero basic recipe figur2 2.6

# LED so wear your safety glasses!
#-----------------------------------------------------------

# Import LED, Button and pause functions only... not the entire
# libraries. Same as in the 01_ scripts, but now including the
# 'Button' function
from gpiozero import LED, Button
from signal import pause

# Set input pins for the button and the led
myLed = LED(17) # GPIO17 / pin 11 
myButton = Button(2) # GPIO18 / pin 12

# Use existing gpiozero functions to turn LED on/off via a button press
myButton.when_pressed = myLed.on
myButton.when_released = myLed.off

# ... to continue running script until killed
pause()

# That's it!  The 'when_pressed' and 'when_released' functions
# take care of almost everything.
