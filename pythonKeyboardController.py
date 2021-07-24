from pynput.keyboard import Key, Controller
from discord import utils
import threading
import random
import time
import os
FLAG = True

counter = 0
first = 0
last = 0

current_time = time.strftime("%H:%M:%S", time.localtime())
print('-'*33)
print(f'The time of starting is: {current_time}')
print('-'*33 + '\n\n')

def send(message):
    keyboard1 = Controller()

    keyboard1.type(message)
    keyboard1.press(Key.enter)
    keyboard1.release(Key.enter)

def beg_loop():
    while FLAG:
        send('pls beg')
        send('pls dep all')

        time.sleep(random.randint(46, 50))

def search_loop(counter, first, last):
    time.sleep(5)

    while FLAG:
        send('pls search')
        time.sleep(5)

        file = open(os.path.join(os.path.dirname(__file__), 'recent.txt'), 'r')
        message = file.read()

        clean_message = utils.remove_markdown(message)
        print(clean_message)

        for i in range(0, len(message)):
            if message[i] == '`':
                if counter == 0:
                    first = i
                    counter += 1
                if counter == 1 or counter == 2:
                    last = i
                    counter += 1

        print(first)
        print(str(last) + '\n')
        print('-'*51 + '\n')

        if first != 0 or last != 0:
            text = message[int(first)+1: int(last)]
            send(text)

        time.sleep(random.randint(29, 33))
        counter = 0


if __name__ == '__main__':
    threads = [threading.Thread(target=beg_loop), threading.Thread(target=search_loop(counter, first, last))]

    for thread in threads:
        thread.start()
