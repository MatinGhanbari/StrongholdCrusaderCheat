from pymem import process, memory as mem, Pymem

from threading import Thread
from time import sleep
from random import Random

from core.utils.base_addresses import *

app_name = 'Stronghold Crusader.exe'
DMC5_base = Pymem(app_name).process_handle


def controlGolds(lord=1, value=Random().randint(2382, 3253)):
    base_address = gold
    increment = 14836
    address = ((lord - 1) * increment) + base_address

    mem.write_int(DMC5_base, address, value)


def controlStockpile(lord=1, value=5000):
    while True:
        mem.write_int(DMC5_base, wood, value)
        mem.write_int(DMC5_base, stone, value)
        mem.write_int(DMC5_base, iron, value)


def controlArmory(lord=1, value=100):
    while True:
        mem.write_int(DMC5_base, bow, value)
        mem.write_int(DMC5_base, spears, value)


def controlGranary(lord=1, value=500):
    while True:
        mem.write_int(DMC5_base, bread, value)
        mem.write_int(DMC5_base, apple, value)
        mem.write_int(DMC5_base, cheese, value)
        mem.write_int(DMC5_base, meat, value)


def mainLoop():
    Thread(target=controlStockpile).start()
    Thread(target=controlGranary).start()
    Thread(target=controlArmory).start()

    while True:
        controlGolds()
        sleep(5)


if __name__ == '__main__':
    print("cheat is active!")
    mainLoopThread = Thread(target=mainLoop, args=(), name='mainLoop Thread')
    mainLoopThread.start()

    mainLoopThread.join()
