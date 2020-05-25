#-----------------------------------------------------------
# File name   : 03_buzzer_0.py
# Description : Wire up a simple on/off buzzer to play when
#               the script runs.
# Wiring      : Run a connection from the GPIO18 pin into the
#               positive end of the buzzer, then close the circuit
#               by tieing the negative end into ground.
#
# Pretty boring, but make buzzer sound programatically.
#-----------------------------------------------------------

# Import Buzzer  and pause functions only... not the entire libraries
from gpiozero import Buzzer
from signal import pause

# Set pins for Buzzer control
myBuzz = Buzzer(18) # GPIO18 / pin 12 

# Use included function 'beep' to play the sound
# parameters are beep(on_time, off_time, repeat), with time in seconds
myBuzz.beep(0.5, 1, 3) # buzz for 1/2 second, off for 1 second, repeat 3 timesz

# ... to keep script running. That's it.
pause()
