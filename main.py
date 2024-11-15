import pyautogui
import time
import pyscreeze
from python_imagesearch.imagesearch import *

def refresh():
    '''
    if nothing is found, refresh
    '''
    try:
        refresh_button = pyscreeze.locateOnScreen("./imgs/refresh.png", confidence=0.8)
        pyautogui.click(refresh_button)
        time.sleep(0.14)
        confirm = pyscreeze.locateOnScreen("./imgs/confirm2.png", confidence=0.8)
        pyautogui.click(confirm)
    except Exception:
        refresh()


def scroll():
    '''
    scroll down
    '''
    pyautogui.scroll(-1000)

def buybuttons(top, height, type):
    '''
    find buy button that is in the same row as the mats
    '''
    confirm = pyscreeze.locateAllOnScreen("./imgs/confirm.png", confidence=0.8)
    for button in confirm:
        if top - (height/2) <=button[1] <= top +height:
            pyautogui.click(button)
    if type == 0:
        buy()
    elif type == 1: 
        buy_mystic()
def covenant():
        location = pyscreeze.locateOnScreen("./imgs/covenant.png", confidence=0.8)
        # center = pyautogui.center(location)
        top = location[1]
        height = location[3]
        #buy()
        buybuttons(top, height, 0)
def mystic():
    location = pyscreeze.locateOnScreen("./imgs/mystics.png", confidence=0.8)
    # center = pyautogui.center(location)
    top = location[1]
    height = location[3]
    #buy_mystic()
    buybuttons(top, height, 1)

def buy():
    try:
        type = pyscreeze.locateOnScreen("./imgs/covenant.png", confidence=0.8)
    except Exception:
        cancel = pyscreeze.locateOnScreen("./imgs/cancel.png", confidence=0.8)
        pyautogui.click(cancel)
    else:
        buy = pyscreeze.locateOnScreen("./imgs/buy_covenant.png", confidence=0.8)
        pyautogui.click(buy)
def buy_mystic():
    try:
        type = pyscreeze.locateOnScreen("./imgs/mystics.png", confidence=0.8)
    except Exception:
        cancel = pyscreeze.locateOnScreen("./imgs/cancel.png", confidence= 0.8)
        pyautogui.click(cancel)
    else:
        buy = pyscreeze.locateOnScreen("./imgs/buy_mystic.png", confidence=0.8)
        pyautogui.click(buy)
def confirm():
    pass

def search():
    time.sleep(0.15)
    try:
        covenant()
    except Exception:
        pass
    finally:
        try:
            mystic()
        except Exception:
            pass
def main():
    time.sleep(0.5)
    search()
    scroll()
    search()
    refresh()
    main()
main()