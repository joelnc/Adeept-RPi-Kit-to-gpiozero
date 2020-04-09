from gpiozero import LED
from signal import pause

myLed = LED(17) 

myLed.blink(.5) 

pause()

