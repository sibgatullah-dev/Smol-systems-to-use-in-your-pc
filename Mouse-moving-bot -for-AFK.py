import pyautogui as pag
import random
import time

while True:
    x = random.randint(700,800)
    y = random.randint(300,650)
    pag.moveTo(x,y,0.5)
    time.sleep(1.5)