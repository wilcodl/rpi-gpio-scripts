#!/usr/bin/python3

import paho.mqtt.subscribe as mqttsub

MQTT_HOST = "10.0.0.44"
MQTT_TOPIC = "ha/fan/mechanische_afzuiging/#"

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))

mqttsub.callback(print_msg, MQTT_TOPIC, hostname=MQTT_HOST)