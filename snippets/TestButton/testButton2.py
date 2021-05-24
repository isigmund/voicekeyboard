#!/usr/bin/env python3
#
# file: add_event_detected-rising-fix.py
#
# add_event_detected solution for rising edges
# a rising edge is detected at approx. 1.25V
#
# you can optionally use GPIO.remove_event_detect(Input_Sig)
#
__author__ = 'paulv'

import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BCM)

Input_Sig = 10 # any plain GPIO pin
# if there is no external pull, use the internal one (pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(Input_Sig, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# set up the edge detection
GPIO.add_event_detect(Input_Sig, GPIO.RISING, bouncetime=200)


def main():

    try:
        while True:
            pass # your code

            if GPIO.event_detected(Input_Sig):
                # if we're here, an edge was detected
                sleep(0.0050) # debounce for 5mSec
                # only show valid edges
                if GPIO.input(Input_Sig) == 1:
                    print ("RISING")
                else:
                    print ("FALLING")

    except KeyboardInterrupt:
        pass
    finally:
        print ("\nRelease the used pin(s)")
        GPIO.cleanup([Input_Sig])


if __name__ == '__main__':
    main()

