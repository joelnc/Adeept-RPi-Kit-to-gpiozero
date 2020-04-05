#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from subprocess import call

##PIR_OUT_PIN = 21    # pin11
PIR_OUT_PIN = 7 # this is GPIO4, physical pin 7

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(PIR_OUT_PIN, GPIO.IN)    # Set BtnPin's mode is input

def loop():
	while True:
		if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
	                print '...Movement not detected!'
		else:
                        # call(["aplay", "-i", "/home/jen/Musette_Appendix_126.wav"])
                        call(["aplay", "-i", "/home/jen/camera-shutter-click-02.wav"])
			# print 'Movement detected!...'

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

