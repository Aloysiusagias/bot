import ctypes
from PIL.ImageOps import grayscale
import pyautogui
import win32api, win32con
import time
import keyboard
from PIL import Image
import ctypes
import pydirectinput

# def click(x,y):
#     print('jalan1')
#     ctypes.windll.user32.SetCursorPos(x, y)
#     time.sleep(1)
#     # pyautogui.click()
#     # win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#     # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     # time.sleep(0.1)
#     # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#     # # pydirectinput.click()
#     # time.sleep(1)

# time.sleep(3)
# selesai = pyautogui.locateCenterOnScreen('selesai event.png', grayscale=True, confidence=0.6)
# print(selesai)
# x, y = selesai
# click(int(x), int(y))


print('Pencet spasi')
time.sleep(3)
# pyautogui.press('a')
pyautogui.write('Hello There')
pydirectinput.press('j')
