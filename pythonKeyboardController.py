from pynput.keyboard import Key, Controller
import time
import threading
import os

import time
import re
import random

flag = True
counter = 0
first = 0
last = 0

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

flag = True
time.sleep(1)
keyboard1 = Controller()


def send(message):
    keyboard1.type(message)
    keyboard1.press(Key.enter)
    keyboard1.release(Key.enter)



def begLoop():
    while flag:
        send("pls beg")
        send("pls dep all")
        time.sleep(random.randint(46, 50))
def searchLoop(counter, first, last):
    time.sleep(5)
    while flag:
        send('pls search')
        time.sleep(5)
        file = open('recent.txt', 'r')
        message = file.read()
        print(message)
        for i in range(0, len(message)):
            if message[i] == '`':
                if counter == 0:
                    first = i
                    counter += 1
                if counter == 1 or counter == 2:
                    last = i
                    counter += 1
        print(first)
        print(last)
        if first != 0 or last != 0:
            text = message[int(first)+1: int(last)]
            send(text)
        time.sleep(random.randint(29, 33))
        counter = 0


time.sleep(5)

thread1 = threading.Thread(target=begLoop)
thread1.start()

thread2 = threading.Thread(target=searchLoop(counter, first, last))
thread2.start()



