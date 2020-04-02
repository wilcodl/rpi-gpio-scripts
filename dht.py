import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

#print humidity

if humidity is not None and temperature is not None:
	humidity = round(humidity, 2)
	temperature = round(temperature, 2)

	print 'Temperatuur: {0:0.1f}*C'.format(temperature)
	print 'Luchtvochtigheid: {0:0.1f}%'.format(humidity)

else:
	print 'Geen data ontvangen'
