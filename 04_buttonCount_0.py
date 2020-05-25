#-----------------------------------------------------------
# File name   : 04_buttonCount_0.py
# Description : Print count to shell.
# Wiring      : See gpiozero basic recipe figure 2.6
#
# Still and LED project, wear your safety glasses
#-----------------------------------------------------------

# Import LED, Button and pause functions only... not the entire libraries
from gpiozero import Button
from signal import pause

# Set pins for button and LED control
myButton = Button(21) # GPIO21 

# Define a custom function named 'myButtonPress' that will
# (1) print a statement and (2) run the command to turn on
# the LED when the function is called

myCount = 1

def myButtonPress():
        global myCount
        print("Count at: " + str(myCount))
        myCount = myCount + 1
        return myCount

def myReact():
        checkVar = myButtonPress()
        if checkVar == 3:
                print("yay")


# When the button is pressed, run our button pressed function
myButton.when_pressed = myButtonPress
myButton.when_pressed = myReact

# ... to keep script running
pause()
