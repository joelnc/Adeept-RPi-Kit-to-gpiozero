from gpiozero import LED, Button
from signal import pause

def lightOn():
        led.on

def lightOff():
        led.off
        
led = LED(26) # GPIO26 / pin 37 
button = Button(21) # GPIO21 / pin 40

button.when_pressed = lightOn
button.when_released = lightOff

pause()
