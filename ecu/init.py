import json
import os
import time
import random
from pynput import keyboard

with open("/Users/mbymax/Documents/code/ecu/ecu/val/basevalues.json", "r") as bv:
    bv = json.load(bv)

rpm = bv['rpm']
speed = bv['speed']
boost = bv['boost']

if not all(var == 0 for var in [rpm, speed, boost]):
    raise ValueError("Init variables are not 0, Killing ignition (E1A01)")

def on_press(key):
    try:
        if key.char == 'r':
            print(f"Current RPM: {rpm}")
    except AttributeError:
        pass

print("Starting RPM increase cycle")

listener = keyboard.Listener(on_press=on_press)
listener.daemon = True  # This allows the listener to run in the background
listener.start()

while rpm < 900:
    rpm_increase = random.choice([50, 100])
    rpm += rpm_increase
    print(f"RPM: {rpm}")

    wait_time = random.uniform(0.1, 0.2)
    time.sleep(wait_time)

# The listener will continue running in the background, even after the RPM reaches 900
listener.join()
