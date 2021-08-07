import ctypes
from PIL.ImageOps import grayscale
import pyautogui
import win32api, win32con
import time
import keyboard
from PIL import Image
import ctypes
import pydirectinput
import random
from counter import detect

def clickBiasa(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    b = round(random.uniform(0.4, 0.6), 2)
    time.sleep(b)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    b = round(random.uniform(0.1, 0.2), 2)
    time.sleep(b)
   

def click(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    b = round(random.uniform(1.5, 2), 2)
    time.sleep(b)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    b = round(random.uniform(0.1, 0.2), 2)
    time.sleep(b)


time.sleep(3)

def bfg():
    while True:
        i = 0
        while True:
            clickBiasa(905,1003)
            clickBiasa(864,491)
            clickBiasa(1233,482)
            clickBiasa(761,991)
            click(864,491)
            click(1233,482)
            print(i)
            i+=1
            detect()
        time.sleep(3)
        pyautogui.keyDown('d')
        b = round(random.uniform(1.5, 2), 2)
        time.sleep(b)
        pyautogui.keyUp('d')
        time.sleep(1)
        detect()
        time.sleep(1)
        pyautogui.keyDown('a')
        b = round(random.uniform(1.5, 2), 2)
        time.sleep(b)
        pyautogui.keyUp('a')
        time.sleep(1)