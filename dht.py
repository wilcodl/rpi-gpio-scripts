import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 3)

#print humidity

if humidity is not None and temperature is not None:
  humidity = round(humidity, 2)
  temperature = round(temperature, 2)

  print 'Temperatuur: {0:0.1f}*C'.format(temperature)
  print 'Luchtvochtigheid: {0:0.1f}%'.format(humidity)

else:
  print 'Geen data ontvangen'
