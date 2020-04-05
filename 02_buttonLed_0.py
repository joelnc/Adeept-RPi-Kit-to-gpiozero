#-----------------------------------------------------------
# File name   : 02_buttonLed_0.py
# Description : Turn LED on/off via button press.
# Wiring      : See gpiozero basic recipe figur2 2.6

#-----------------------------------------------------------

# Import LED, Button and pause functions only... not the entire libraries
from gpiozero import LED, Button
from signal import pause

# Set input pins for button and led
myLed = LED(17) # GPIO17 / pin 11 
myButton = Button(2) # GPIO18 / pin 12

# Use existing functions to turn LED on/off via button press
myButton.when_pressed = myLed.on
myButton.when_released = myLed.off

# ... to continue running script until killed
pause()
