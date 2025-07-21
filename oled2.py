from machine import Pin, SoftI2C
import ssd1306
import dht
from time import sleep

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(27))

while 1:
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    display.fill(0)
    display.text('Temp :', 10, 20, 1)
    display.text(str(int(temperature)) + '*C', 65, 20, 1)
    display.text('Humi : ', 10, 44, 1)
    display.text(str(humidity) + '%', 65, 44, 1)
    display.show()
    sleep(1)
