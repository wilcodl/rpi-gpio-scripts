#!/usr/bin/python3

from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(4)

while True:
	buzzer.on()
	sleep(1)
	buzzer.off()
	sleep(1)