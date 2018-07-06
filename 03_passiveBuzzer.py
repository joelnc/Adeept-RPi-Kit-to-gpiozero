#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 12

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ.... speed!
p.start(50)  # Duty cycle: 50%

try:
	while True:
                ## Trying to play happy birthday...
                for f in [400,400,600,400,900,800,1, 400,400,600,400,1100,900,1]:
                        p.ChangeFrequency(f)
                        print(f)
                        time.sleep(0.5)
                ## Original code        
# 		for f in range(100, 2000, 100):
# 			p.ChangeFrequency(f)
#                         print(f)
# 			time.sleep(0.5)
# 		for f in range(2000, 100, -100):
# 			p.ChangeFrequency(f)
# 			time.sleep(0.5)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
