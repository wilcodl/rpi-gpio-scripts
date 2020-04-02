#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

counter = 0

GPIO.setmode(GPIO.BOARD)
PIN = 12
GPIO.setup(PIN, GPIO.OUT)

try:
  while True:
	GPIO.output(PIN, True)
	time.sleep(5)

	GPIO.output (PIN, False)
	time.sleep(5)

	counter += 1
  
except KeyboardInterrupt:  
	# here you put any code you want to run before the program   
	# exits when you press CTRL+C  
	print("\nCounter: %s" % counter) # print value of counter  
  
except:  
	# this catches ALL other exceptions including errors.  
	# You won't get any error messages for debugging  
	# so only use it once your code is working  
	print("Other error or exception occurred!")
  
finally:  
	GPIO.cleanup() # this ensures a clean exit

