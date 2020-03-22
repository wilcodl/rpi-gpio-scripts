#!/usr/bin/python3

import RPi.GPIO as GPIO
import paho.mqtt.publish as mqttpub # sudo apt install python3-paho-mqtt
import paho.mqtt.subscribe as mqttsub
import time

def change_fan(client, userdata, message):
	value = message.payload.decode("utf-8")
	# print(value)

	if message.topic == 'ha/fan/mechanische_afzuiging/on/set':

		if value == 'false':
			print('Off')
			GPIO.output(PIN1, OFF)

			mqttpub.single(MQTT_ON_TOPIC, "false", hostname=MQTT_HOST)
		elif value == 'true':
			print('On')
			GPIO.output(PIN1, ON)

			mqttpub.single(MQTT_ON_TOPIC, "true", hostname=MQTT_HOST)
		else:
			print('Invalid on input')
	
	elif message.topic == 'ha/fan/mechanische_afzuiging/speed/set':
		
		if value == 'low':
			print('Low')
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, OFF)

			mqttpub.single(MQTT_SPEED_TOPIC, "low", hostname=MQTT_HOST)
		elif value == 'medium':
			print('Medium')
			GPIO.output(PIN2, ON)
			GPIO.output(PIN3, OFF)

			mqttpub.single(MQTT_SPEED_TOPIC, "medium", hostname=MQTT_HOST)
		elif value == 'high':
			print('High')
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, ON)

			mqttpub.single(MQTT_SPEED_TOPIC, "high", hostname=MQTT_HOST)
		else:
			print('Invalid speed input')

	time.sleep(0.1)


PIN1 = 11 # On / Off
PIN2 = 12 # Medium
PIN3 = 13 # High
ON = False
OFF = True # Hoog is relay uit

MQTT_HOST = "10.0.0.44"
MQTT_SPEED_TOPIC = "ha/fan/mechanische_afzuiging/speed/state"
MQTT_ON_TOPIC = "ha/fan/mechanische_afzuiging/on/state"
MQTT_TOPIC = "ha/fan/mechanische_afzuiging/#"

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN3, GPIO.OUT, initial=GPIO.HIGH)

try:
	mqttsub.callback(change_fan, MQTT_TOPIC, hostname=MQTT_HOST)

except KeyboardInterrupt:
	print("\nKeyboardInterrupt")
  
except:
	print("Other error or exception occurred!")
  
finally:
	GPIO.cleanup()