import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

def get_AC_current(sensitivity,Vref,averageVValue):
	'''
	5A current sensor AC output and get n chanel data with unit mA.
	:param float sensitivity: The coefficient by which voltage is converted into current.
	:param int Vref: Initial voltage at no load.
	:param int averageValue: Average acquisition frequency.
	Returns: 
		int: current value
	'''
	sensorValue = 0
	for i in range(averageValue):
		val = chan0.voltage * 1000

		if (val > sensorValue):
			sensorValue = val
		time.sleep(0.00004)
	currentVal = ((sensorValue - Vref) * sensitivity)*0.707
	return currentVal

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P1)

print('ADC Voltage: ' + str(chan0.voltage) + 'V')


sensitivity = 1000.0 / 200.0
Vref = 1498
averageValue = 500

# mV = chan0.voltage * 1000
# currentVal = ((mV - Vref) * sensitivity)*0.707
# print('Current: ' + str(currentVal) + 'mA')

current = get_AC_current(sensitivity,Vref,averageValue)

print("current (mA): " + str(current))