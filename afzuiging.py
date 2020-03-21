#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys

# 0: Off
# 1: Low
# 2: Medium
# 3: High

PIN1 = 11 # On / Off
PIN2 = 12 # Medium
PIN3 = 13 # High
ON = False
OFF = True # Hoog is relay uit

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN3, GPIO.OUT, initial=GPIO.HIGH)

if sys.argv[1] == '0':
	print('Off')
	# GPIO.output(PIN1, OFF)
elif sys.argv[1] == '1':
	print('Low')
	GPIO.output(PIN1, ON)
elif sys.argv[1] == '2':
	print('Medium')
	GPIO.output(PIN1, ON)
	GPIO.output(PIN2, ON)
elif sys.argv[1] == '3':
	print('High')
	GPIO.output(PIN1, ON)
	GPIO.output(PIN3, ON)
else:
	print('Invalid input')


# time.sleep(1)

# GPIO.cleanup()