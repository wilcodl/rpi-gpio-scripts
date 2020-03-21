#!/usr/bin/python3

import RPi.GPIO as GPIO
import paho.mqtt.publish as mqttpub # sudo apt install python3-paho-mqtt

# 0: Off
# 1: Low
# 2: Medium
# 3: High

PIN1 = 11 # On / Off
PIN2 = 12 # Medium
PIN3 = 13 # High
ON = False
OFF = True # Hoog is relay uit

MQTT_HOST = "10.0.0.44"
MQTT_TOPIC = "relay/fan/mode"

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN3, GPIO.OUT, initial=GPIO.HIGH)

try:
	while True:
		mode = input("Mode: ")

		if mode == '0':
			print('Off')
			GPIO.output(PIN1, OFF)

			mqttpub.single(MQTT_TOPIC, "off", hostname=MQTT_HOST)
		elif mode == '1':
			print('Low')
			GPIO.output(PIN1, ON)
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, OFF)

			mqttpub.single(MQTT_TOPIC, "low", hostname=MQTT_HOST)
		elif mode == '2':
			print('Medium')
			# GPIO.output(PIN1, ON)
			GPIO.output(PIN2, ON)
			GPIO.output(PIN3, OFF)

			mqttpub.single(MQTT_TOPIC, "medium", hostname=MQTT_HOST)
		elif mode == '3':
			print('High')
			# GPIO.output(PIN1, ON)
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, ON)

			mqttpub.single(MQTT_TOPIC, "high", hostname=MQTT_HOST)
		else:
			print('Invalid input')

except KeyboardInterrupt:
	print("\nKeyboardInterrupt")
  
except:
	print("Other error or exception occurred!")
  
finally:
	GPIO.cleanup()