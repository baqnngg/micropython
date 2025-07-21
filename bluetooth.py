import time

import ble_library

import bluetooth



ble = bluetooth.BLE()

p = ble_library.BLESimplePeripheral(ble, "jung sik")



def on_rx(v):

    print("수신", v)



p.on_write(on_rx)