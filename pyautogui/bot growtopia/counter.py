import pyautogui
import numpy as np
from PIL import ImageGrab, Image
import cv2
from numpy.core.defchararray import split
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import ctypes
from PIL.ImageOps import grayscale
import win32api, win32con
import time
import keyboard
import pydirectinput
import random

def img_to_text(img):
    # img = Image.open('model.PNG')
    text = tess.image_to_string(img)
    # text = "\n".split(text)
    for x in text:
        c = x.isascii()
        if not c:
            text = text.replace(x, '')
    text = text[:-2]
    return text

def click(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    b = round(random.uniform(0.4, 0.6), 2)
    time.sleep(b)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    b = round(random.uniform(0.2, 0.5), 2)
    time.sleep(b)

def detect():
    if(pyautogui.locateOnScreen('tambah2.png', confidence=0.5) != None):
        x1, y1, x, y = pyautogui.locateOnScreen('tambah2.png', confidence=0.8)
        x2 = x1 + x
        y2 = y1 + y
        y1 = y1 + 200
        y2 = y2 - 200
        x1 = x1 + 15
        x2 = x2 - 1150
        answerX = x2 + 115
        answerY = y2 + 30
        submitX = x2 - 85
        submitY = y2 + 100
        print(x2, y2)
        screen = np.array(ImageGrab.grab(bbox=(x1,y1,x2,y2)))
        teks = img_to_text(screen)
        angka = teks.split("+")
        hasil = int(angka[0]) + int(angka[1])
        print('|'+teks+'|')
        print(angka)
        print(hasil)
        click(int(answerX), int(answerY))
        time.sleep(0.25)
        pyautogui.write(str(hasil))
        time.sleep(0.25)
        click(int(submitX), int(submitY))
        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    else :
        print("tidak terdeteksi")

detect()

# x1, y1, x, y = pyautogui.locateOnScreen('tambah2.png', confidence=0.8)
# x2 = x1 + x
# y2 = y1 + y
# # y1 = y1 + 180
# # y2 = y2 - 50
# # x1 = x1 + 10
# # x2 = x2 - 800
# # click(int(x2), int(y2))
# # print(x2,y2)
# y1 = y1 + 200
# y2 = y2 - 200
# x1 = x1 + 15
# x2 = x2 - 1150
# answerX = x2 + 115
# answerY = y2 + 30
# submitX = x2 - 85
# submitY = y2 + 100
# click(int(answerX), int(answerY))
# while(True):
#     screen = np.array(ImageGrab.grab(bbox=(x1,y1,x2,y2)))
#     cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break