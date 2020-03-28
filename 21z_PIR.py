#!/usr/bin/env python

from gpiozero import MotionSensor, LED
import time
from subprocess import call
from signal import pause

pir = MotionSensor(4) # as in pin 7

def play_click():
        call(["aplay","-i","/home/jen/camera-shutter-click-02.wav"])


pir.when_motion = play_click
        
#if !(pir.motion_detected):
##        call(["aplay", "-i", "/home/jen/camera-shutter-click-02.wav"])

## Works!!
#wait_for_motion = call(["aplay", "-i", "/home/jen/camera-shutter-click-02.wav"])


##if when_motion:
  ##      call(["aplay", "-i", "/home/jen/camera-shutter-click-02.wav"])

pause()

# def loop():
# 	while True:
#                 if pir.when_motion:
#                         call(["aplay", "-i", "/home/jen/camera-shutter-click-02.wav"])
#                 else:
#                         print('...Movement not detected!')

# 		# if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
# 	        #         print '...Movement not detected!'
# 		# else:
#                 #         # call(["aplay", "-i", "/home/jen/Musette_Appendix_126.wav"])
#                 #         call(["aplay", "-i", "/home/jen/camera-shutter-click-02.wav"])
# 		# 	# print 'Movement detected!...'


# if __name__ == '__main__':     # Program start from here
# 	try:
# 		loop()
# 	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
# 		destroy()

