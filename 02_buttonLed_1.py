#-----------------------------------------------------------
# File name   : 02_buttonLed_1.py
# Description : Turn LED on/off via button press.
# Wiring      : See gpiozero basic recipe figure 2.6

#-----------------------------------------------------------

# Import LED, Button and pause functions only... not the entire libraries
from gpiozero import LED, Button
from signal import pause

# Set pins for button and led control
myLed = LED(17) # GPIO26 / pin 37 
myButton = Button(2) # GPIO21 / pin 40

# Use the gpiozero 'source' function to set the control for the
# LED to by myButton.... that's it!
myLed.source = myButton

# To keep script running
pause()
