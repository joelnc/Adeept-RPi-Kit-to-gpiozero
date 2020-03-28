# From gpiozero documentation

from gpiozero import LED
from time import sleep

led = LED(26) # pin 37

while True:
        led.on()
        sleep(1) # timing in seconds
        led.off()
        sleep(1)
