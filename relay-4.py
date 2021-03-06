#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

counter = 0

PIN1 = 11
PIN2 = 12
PIN3 = 13
# PIN4 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN3, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(PIN4, GPIO.OUT)

GPIO.output(PIN1, False)

try:
	while True:
		# GPIO.output(PIN1, True)
		# GPIO.output(PIN2, True)
		# GPIO.output(PIN3, True)


		# GPIO.output(PIN1, True)
		# time.sleep(5)

		# GPIO.output (PIN1, False)
		time.sleep(5)

		counter += 1
		
  
except KeyboardInterrupt:
	print("\nCounter: %s" % counter)
  
except:
	print("Other error or exception occurred!")
  
finally:
	GPIO.cleanup()
