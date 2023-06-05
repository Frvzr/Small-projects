import pyautogui as pag
from random import randint, choice
import logging
from datetime import datetime


KEYS = ['f15', 'f17', 'f18', 'f19']
pag.FAILSAFE = False
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def get_random(func):
    def wrapper():
        min_move = randint(-30, 30)
        max_move = randint(-30, 30)
        key = choice(KEYS)
        pause_time = randint(100, 150)
        try:
            result = func(min_move, max_move, pause_time)
        except:
            result = func(key, pause_time)
        return result
    return wrapper

def get_exeption(e):
    logging.exception('Произошла ошибка: %s', e)
    exit()

@get_random
def move_mouse(min_move, max_move, pause_time):
    try:
        print(f'Change mouse position after {pause_time} sec')
        pag.PAUSE = pause_time
        pag.moveRel(min_move, max_move, 0.1)
    except Exception as e:
        get_exeption(e)
    
@get_random
def press_key(key, pause_time):
    try:
        print(f'{key} will be presseed after {pause_time} sec')
        pag.PAUSE = pause_time
        pag.press(key)
    except Exception as e:
        get_exeption(e)
        

def main():
    try:
        move_mouse()
        press_key()
    except Exception as e:
        get_exeption(e)
        
if __name__ == '__main__':
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info('Start programm')
    print(f'Start time: {start_time}')
    while True:
        main()
    