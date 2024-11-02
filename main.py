from characters import set_character
import time
from machine import Timer
from micropython import const

class Mode:
    DEFAULT = 0
    NAME_BADGE = 1

MODE = Mode.DEFAULT


def update_mode():
    global MODE

    if buttonA.value() == 0 and MODE != Mode.DEFAULT:
        print('Going to default mode')
        MODE = Mode.DEFAULT
    elif buttonB.value() == 0 and MODE != Mode.NAME_BADGE:
        print('Going to name badge mode')
        MODE = Mode.NAME_BADGE

NAME = 'BEN'
NAME_CHARACTERS = list(NAME)
position = 0


def timer_tick(t):
    global MODE
    global position

    if MODE == Mode.NAME_BADGE:
        position += 1
        if position >= len(NAME_CHARACTERS):
            position = 0
        
        set_character(petal_bus, NAME_CHARACTERS[position])
    elif MODE == Mode.DEFAULT:
        pass


def original_loop():
    ## display button status on RGB
    if petal_bus:
        if not buttonA.value():
            petal_bus.writeto_mem(PETAL_ADDRESS, 2, bytes([0x80]))
        else:
            petal_bus.writeto_mem(PETAL_ADDRESS, 2, bytes([0x00]))

        if not buttonB.value():
            petal_bus.writeto_mem(PETAL_ADDRESS, 3, bytes([0x80]))
        else:
            petal_bus.writeto_mem(PETAL_ADDRESS, 3, bytes([0x00]))

        if not buttonC.value():
            petal_bus.writeto_mem(PETAL_ADDRESS, 4, bytes([0x80]))
        else:
            petal_bus.writeto_mem(PETAL_ADDRESS, 4, bytes([0x00]))

    ## see what's going on with the touch wheel
    if touchwheel_bus:
        tw = touchwheel_read(touchwheel_bus)

    ## display touchwheel on petal
    if petal_bus and touchwheel_bus:
        if tw > 0:
            tw = (128 - tw) % 256 
            petal = int(tw/32) + 1
        else: 
            petal = 999
        for i in range(1,9):
            if i == petal:
                petal_bus.writeto_mem(0, i, bytes([0x7F]))
            else:
                petal_bus.writeto_mem(0, i, bytes([0x00]))


    
    time.sleep_ms(100)
    bootLED.off()

if __name__ == '__main__':
    tim = Timer()

    tim.init(period=700, mode=Timer.PERIODIC, callback=timer_tick)

    while True:
        update_mode()

        if MODE == Mode.DEFAULT:
            original_loop()