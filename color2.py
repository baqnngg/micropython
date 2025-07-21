from machine import Pin, SoftI2C
from tcs34725 import TCS34725
from neopixel import NeoPixel
import time

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
tcs = TCS34725(i2c)

npPin = Pin(14, Pin.OUT)
np = NeoPixel(npPin, 12)

tcs.gain(1)
tcs.integration_time(240)

while 1:
    value = tcs.read("rgb")
    print('rgb :', value)

    max_value = max(value[0:3])
    color_index = value.index(max_value)
    print('color_index :', color_index)


    if color_index == 0:
        for i in range(0,12):
            np[i] = (255,0,0)
        np.write()
    elif color_index == 1:
        for i in range(0,12):
            np[i] = (0,255,0)
        np.write()
    elif color_index == 2:
        for i in range(0,12):
            np[i] = (0,0,255)
        np.write()
