# Ultimate starter kit
https://nl.banggood.com/Ultimate-Starter-Kit-DIY-Projects-Student-Education-Program-For-Raspberry-Pi-3-p-1235892.html

### SMB share instellen
```shell
sudo apt update
sudo apt-get remove -y --purge man-db
sudo apt install samba

sudo vi /etc/samba/smb.conf

[python]
    comment = Samba on Ubuntu
    path = /home/pi/python
    read only = no
    browsable = yes

sudo service smbd restart

sudo smbpasswd -a pi
```

### DHT11 vochtsensor
http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

### MCP3008 ADC
https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi

### Mercury Switch Sensor Module
https://osoyoo.com/2016/04/08/get-input-signal-from-raspberry-pi-gpio/

### GY-302 (BH1750) lichtsensor
http://domoticx.com/raspberry-pi-lichtsensor-bh1750-gy-302/

1. I2C bus aanzetten via raspi-config
2. vereisten installeren en testen:
```shell
sudo apt-get install python-smbus i2c-tools
sudo i2cdetect -y 1
```
3. gy302 draaien

### Actieve buzzer

https://raspberrytips.nl/zoemer-buzzer-gpio-zero-raspberry-pi/

```shell
sudo apt install python3-gpiozero
```

buzzer.py

### Passieve buzzer
https://github.com/gumslone/raspi_buzzer_player

```shell
wget https://raw.githubusercontent.com/gumslone/raspi_buzzer_player/master/buzzer_player.py
```

### 4 Relay Module
https://nl.banggood.com/5V-4-Channel-Relay-Module-For-PIC-ARM-DSP-AVR-MSP430-Blue-p-87987.html
http://wiki.sunfounder.cc/index.php?title=4_Channel_5V_Relay_Module

/relay-4.py