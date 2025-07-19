from machine import Pin
import dht
import time

d = dht.DHT11(Pin(27))

while 1:
    d.measure()
    print("온도 값 :",d.temperature())
    print("습도 값 :",d.humidity())
    print()
    time.sleep(1)