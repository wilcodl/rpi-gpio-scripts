# HC-SR501 motion sensor 
# https://raspberrytips.nl/hc-sr501-bewegingssensor-pir-raspberry-pi/


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#PIN = 26
PIN = 11
GPIO.setup(PIN, GPIO.IN)

print "Start sensor..."
time.sleep(2)
print "Sensor activated..."

while True:
   if GPIO.input(PIN):
      print "Movement detected! " + (time.strftime("%H:%M:%S"))
      time.sleep(2)
   time.sleep(0.1)
