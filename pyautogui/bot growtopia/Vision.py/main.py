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
# import mss


while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
    player = cv2.imread('playerKecilKiri.png')
    w = player.shape[1]
    h = player.shape[0]
    result = cv2.matchTemplate(screen, player, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    cv2.rectangle(screen, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
    print(max_val)
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break