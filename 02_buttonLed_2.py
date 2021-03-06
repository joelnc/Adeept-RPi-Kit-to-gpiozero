#-----------------------------------------------------------
# File name   : 02_buttonLed_2.py
# Description : Turn LED on/off via button press using custom
#               functions that can do more than 1 thing.
# Wiring      : See gpiozero basic recipe figure 2.6
#
# Still and LED project, wear your safety glasses
#-----------------------------------------------------------

# Import LED, Button and pause functions only... not the entire libraries
from gpiozero import LED, Button
from signal import pause

# Set pins for button and LED control
myLed = LED(17) # GPIO17 / pin 11 
myButton = Button(2) # GPIO2 / pin 3

# Define a custom function named 'myButtonPress' that will
# (1) print a statement and (2) run the command to turn on
# the LED when the function is called
def myButtonPress():
        print("Button is being pressed....light ON")
        myLed.on()

# Define another function to print something and turn
# off the LED when called
def myButtonRelease():
        print("Button has been released.... light OFF")
        myLed.off()
        
# When the button is pressed, run our button pressed function
myButton.when_pressed = myButtonPress
# When the button is released, run our button released function
myButton.when_released = myButtonRelease

# ... to keep script running
pause()
