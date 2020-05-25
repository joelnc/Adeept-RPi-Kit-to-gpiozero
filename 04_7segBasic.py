#-----------------------------------------------------------
# File name   : 04_7segBasic.py
# Description : Display digits.
# Wiring      : See Run a connection from the GPIO18 pin into the
#               positive end of the buzzer, then close the circuit
#               by tieing the negative end into ground.
#
# Pretty boring, but make buzzer sound programatically.
#-----------------------------------------------------------

# Import Buzzer  and pause functions only... not the entire libraries
from gpiozero import LED
from signal import pause

#######################
'''
 g  f  gd  a  b
 |  |  |   |  |
 ______________
     -----
    |  a  |
   f|     |b
    |     |
     -----
    |  g  |
   e|     |c
    |     |
     -----
       d    .dp
 ______________
 |  |  |   |  |
 e  d  gd  c  dp
'''


# Set pins for segment control
segG = LED(25) # GPIO25 / pin 22
segF = LED(24)
segA = LED(17)
segB = LED(18)
segE = LED(23)
segD = LED(22)
segC = LED(27)
segDp = LED(4)
 
# Set number to display
showNumber = 4

if showNumber == 0:
    segA.on()
    segB.on()
    segC.on()
    segD.on()
    segE.on()
    segF.on()
elif showNumber == 1:
    segB.on()
    segC.on()
elif showNumber == 4:
    segF.on()
    segG.on()
    segB.on()
    segC.on()
elif showNumber == 7:
    segA.on()
    segB.on()
    segC.on()
elif showNumber == 8:
    segA.on()
    segB.on()
    segC.on()
    segD.on()
    segE.on()
    segF.on()
    segG.on()

# ... to keep script running. That's it.
pause()
