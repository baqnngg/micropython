import time
from machine import Pin
from neopixel import NeoPixel
import math

pin = Pin(14, Pin.OUT)
np = NeoPixel(pin, 12)

touch1 = Pin(33, Pin.IN)
touch2 = Pin(32, Pin.IN)
touch3 = Pin(35, Pin.IN)
touch4 = Pin(34, Pin.IN)

def hsv_to_rgb(h, s, v):
    h = h % 360
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    
    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
        
    return (int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))

rotating_rainbow_offset = 0
RAINBOW_COLORS = [
    (255, 0, 0), (255, 127, 0), (255, 255, 0), (127, 255, 0),
    (0, 255, 0), (0, 255, 127), (0, 255, 255), (0, 127, 255),
    (0, 0, 255), (127, 0, 255), (255, 0, 255), (255, 0, 127)
]

def rotating_rainbow_step():
    global rotating_rainbow_offset
    for i in range(12):
        color_index = (i + rotating_rainbow_offset) % 12
        np[i] = RAINBOW_COLORS[color_index]
    np.write()
    rotating_rainbow_offset = (rotating_rainbow_offset + 1) % 12
    time.sleep(0.05)

def smooth_rainbow_init():
    for i in range(12):
        hue = (i * 360 // 12)
        np[i] = hsv_to_rgb(hue, 1.0, 1.0)
    np.write()
    time.sleep(0.05)

rainbow_chase_start = 0

def rainbow_chase_step():
    global rainbow_chase_start
    for i in range(12):
        np[i] = (0, 0, 0)
        
    for i in range(3):
        pos = (rainbow_chase_start + i) % 12
        np[pos] = RAINBOW_COLORS[pos]
            
    np.write()
    rainbow_chase_start = (rainbow_chase_start + 1) % 12
    time.sleep(0.05)

rainbow_fade_hue_offset = 0
rainbow_fade_step_counter = 0

def rainbow_rotate_fade_step():
    global rainbow_fade_hue_offset, rainbow_fade_step_counter
    
    overall_brightness = (math.sin(rainbow_fade_step_counter * 0.05) + 1) / 2
    
    for i in range(12):
        hue = (rainbow_fade_hue_offset + i * 30) % 360
        np[i] = hsv_to_rgb(hue, 1.0, overall_brightness)
        
    np.write()
    rainbow_fade_hue_offset = (rainbow_fade_hue_offset + 3) % 360
    rainbow_fade_step_counter += 1
    time.sleep(0.05)

current_effect = 'none'

def clear_neopixels():
    for i in range(12):
        np[i] = (0, 0, 0)
    np.write()

clear_neopixels()

while True:
    if touch1.value():
        if current_effect != 'rotating':
            clear_neopixels()
            rotating_rainbow_offset = 0
            current_effect = 'rotating'
        rotating_rainbow_step()
    elif touch2.value():
        if current_effect != 'smooth':
            clear_neopixels()
            smooth_rainbow_init()
            current_effect = 'smooth'
        
    elif touch3.value():
        if current_effect != 'chase':
            clear_neopixels()
            rainbow_chase_start = 0
            current_effect = 'chase'
        rainbow_chase_step()
    elif touch4.value():
        if current_effect != 'none':
            clear_neopixels()
            current_effect = 'none'
    else:
        if current_effect == 'rotating':
            rotating_rainbow_step()
        elif current_effect == 'chase':
            rainbow_chase_step()
        elif current_effect == 'fade':
            rainbow_rotate_fade_step()
        elif current_effect == 'smooth':
            pass
        elif current_effect == 'none':
            clear_neopixels()

    time.sleep(0.01)