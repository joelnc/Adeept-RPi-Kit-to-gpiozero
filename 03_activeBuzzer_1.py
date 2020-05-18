#-----------------------------------------------------------
# File name   : 03_activeBuzzer_1.py
# Description : Modify the buzzer to sound when button is pressed.
#               
# Wiring      : See the Adeept Wiring PNG 02_activeBuzzer.png
#
# Pretty boring, but get introduced to a transistor.
#-----------------------------------------------------------

# Import Buzzer  and pause functions only... not the entire libraries
from gpiozero import Buzzer
from signal import pause

# Set pins for Buzzer control
myBuzz = Buzzer(18) # GPIO18 / pin 12 

# Use included function 'beep' to play the sound
# parameters are beep(on_time, off_time, repeat), with time in seconds
myBuzz.beep(1,1,40)

# ... to keep script running. That's it.
pause()
