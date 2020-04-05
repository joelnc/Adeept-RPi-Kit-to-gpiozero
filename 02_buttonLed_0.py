from gpiozero import LED, Button
from signal import pause

led = LED(26) # GPIO26 / pin 37 
button = Button(21) # GPIO21 / pin 40

button.when_pressed = led.on
button.when_released = led.off

pause()
