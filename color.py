from machine import Pin, SoftI2C
from tcs34725 import TCS34725
import time

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
tcs = TCS34725(i2c)

tcs.gain(1)
tcs.integration_time(240)
print('rgb : ' + str(tcs.read('rgb')))

tcs.gain(4)
tcs.integration_time(480)
print('rgb : ' + str(tcs.read('rgb')))