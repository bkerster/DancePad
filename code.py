# Write your code here :-)
"""CircuitPython Essentials Pin Map Script"""
import time

import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


def get_voltage(pin):
    return (pin.value * 3.3) / 65536

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)

left = AnalogIn(board.A0)
right = AnalogIn(board.A1)
up = AnalogIn(board.A2)
down = AnalogIn(board.A3)

blue = DigitalInOut(board.D6)
blue.direction = Direction.INPUT

red = DigitalInOut(board.D7)
red.direction = Direction.INPUT

key_mapping = {
    'l': Keycode.LEFT_ARROW,
    'r': Keycode.RIGHT_ARROW,
    'u': Keycode.UP_ARROW,
    'd': Keycode.DOWN_ARROW,
    'blue': Keycode.ENTER,
    'red': Keycode.ESCAPE,
}

a_inputs = [left, right, up, down]
states = {'l':0, 'r':0, 'u':0, 'd':0, 'red':0, 'blue':0}
prev_states = {'l':0, 'r':0, 'u':0, 'd':0, 'red':0, 'blue':0}
print("We are Alive!")
while True:
    # check which buttons are pressed
    states = {'l':0, 'r':0, 'u':0, 'd':0, 'red':0, 'blue':0} # resetting each state so I don't need an elif for each button
    if get_voltage(right) < 0.07:
        states['r'] = 1
    if get_voltage(left) < 0.07:
        states['l'] = 1
    if get_voltage(up) < 0.15:
        states['u'] = 1
    if get_voltage(down) < 0.07:
        states['d'] = 1
    if not blue.value:
        states['blue'] = 1
    if not red.value:
        states['red'] = 1

    for k, v in states.items():
        prev_v = prev_states[k]
        if v == 1 and prev_v == 0:
            # new press
            keyboard.press(key_mapping[k])
            #pass
        elif v == 0 and prev_v == 1:
            # press ended
            keyboard.release(key_mapping[k])
            #pass

        prev_states[k] = v

    time.sleep(0.005)

    # debug statement
    #print((states['r'], states['l'], states['u'], states['d'], states['blue'], states['red']))
    #print( tuple([get_voltage(x) for x in a_inputs]) )
    #time.sleep(0.1)


