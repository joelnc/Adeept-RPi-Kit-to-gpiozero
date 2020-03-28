# From gpiozero documentation

from gpiozero import LED
from signal import pause

led = LED(26) # pin 37

led.blink(.1) # arg is timing

pause()

