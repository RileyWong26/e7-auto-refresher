import pyautogui
import time
import pyscreeze
from python_imagesearch.imagesearch import *

#pyautogui.moveTo(1000,100, duration = 0.2)

#pyautogui.leftClick(1000, 100, 2, 1)

# img = imagesearch_loop("./imgs/apple.png", 0.2)
# print(img)
# time.sleep(2)
def refresh():
    '''
    if nothing is found, refresh
    '''
    refresh = pyscreeze.locateOnScreen("./imgs/refresh.png", confidence=0.8)
    pyautogui.click(refresh)
    confirm = pyscreeze.locateOnScreen("./imgs/confirm2.png", confidence=0.8)
    pyautogui.click(confirm)


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
        pyautogui.moveTo(location)
        #buy()
        buybuttons(top, height, 0)
def mystic():
    location = pyscreeze.locateOnScreen("./imgs/mystics.png", confidence=0.8)
    # center = pyautogui.center(location)
    top = location[1]
    height = location[3]
    pyautogui.moveTo(location)
    #buy_mystic()
    buybuttons(top, height, 1)

def buy():
    type = pyscreeze.locateOnScreen("./imgs/covenant.png", confidence=0.8)
    buy = pyscreeze.locateOnScreen("./imgs/buy_covenant.png", confidence=0.8)
    pyautogui.click(buy)
def buy_mystic():
    type = pyscreeze.locateOnScreen("./imgs/mystic.png", confidence=0.8)
    buy = pyscreeze.locateOnScreen("./imgs/buy_mystic.png", confidence=0.8)
    pyautogui.click(buy)
def confirm():
    pass

def main():
    try:
        covenant()
    except Exception:
        print("notfound")
        main()
main()