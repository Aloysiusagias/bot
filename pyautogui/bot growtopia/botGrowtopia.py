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


def click(x,y):
    print('jalan1')
    ctypes.windll.user32.SetCursorPos(x, y)
    a = round(random.uniform(0.25, 0.40), 2)
    time.sleep(a)
    # pyautogui.click(x, y, button='left')
    # win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    b = round(random.uniform(1.5, 1.8), 2)
    time.sleep(b)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    # time.sleep(0.1)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    # pydirectinput.click()

def clickBiasa(x,y):
    print('jalan1')
    ctypes.windll.user32.SetCursorPos(x, y)
    a = round(random.uniform(0.25, 0.40), 2)
    time.sleep(a)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    b = round(random.uniform(0.2, 0.3), 2)
    time.sleep(b)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    b = round(random.uniform(0.2, 0.3), 2)
    time.sleep(b)

time.sleep(2)

hit = [[813,166],[815,288],[811,496],[628,500],[642,344],[643,145]]
while True:
    # pyautogui.screenshot('file.png')
    # img = Image.open('file.png')
    # print(img.getpixel((811,496))[0],1)
    # clickBiasa(863,938)
    # if img.getpixel((811,496))[0]==249:
    #     print(img.getpixel((811,496))[0],2)
    #     while img.getpixel((811,496))[0]==249:
    #         print(img.getpixel((811,496))[0],3)
    #         for i in hit:
    #             click(i[0],i[1])
    #         pyautogui.keyDown('a')
    #         b = round(random.uniform(0.8, 1.2), 2)
    #         time.sleep(b)
    #         pyautogui.keyUp('a')
    #         pyautogui.screenshot('file.png')
    #         img = Image.open('file.png')
    
    # while img.getpixel((1579,457))[0]!=74:
    #     print("Jalan")
    #     pyautogui.screenshot('file.png')
    #     img = Image.open('file.png')
    #     if img.getpixel((1579,457))[0]!=74:
    #         print("Jalan juga")
    #         pyautogui.keyDown('d')
    #         b = round(random.uniform(0.03, 0.05), 2)
    #         time.sleep(b)
    #         pyautogui.keyUp('d')
    #         pyautogui.keyDown('w')
    #         b = round(random.uniform(0.1, 0.18), 2)
    #         time.sleep(b)
    #         pyautogui.keyUp('w')
    
    # pyautogui.keyDown('d')
    # time.sleep(1)
    # pyautogui.keyUp('d')

    # clickBiasa(1069,944)
    # ctypes.windll.user32.SetCursorPos(1205, 485)
    # a = round(random.uniform(0.25, 0.40), 2)
    # time.sleep(a)
    # pyautogui.keyDown('a')
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # b = round(random.uniform(13, 14), 2)
    # time.sleep(b)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    # pyautogui.keyUp('a')

    # clickBiasa(865,938)

    # time.sleep(240)

    # pyautogui.screenshot('file.png')
    # img = Image.open('file.png')

    # while img.getpixel((1554,471))[0]!=74:
    #     print("Jalan12")
    #     pyautogui.screenshot('file.png')
    #     img = Image.open('file.png')
    #     if img.getpixel((1554,471))[0]!=74:
    #         print("Jalan juga")
    #         pyautogui.keyDown('d')
    #         b = round(random.uniform(0.03, 0.05), 2)
    #         time.sleep(b)
    #         pyautogui.keyUp('d')
    #         clickBiasa(1010, 485)
    
    # pyautogui.keyDown('a')
    # time.sleep(14)
    # pyautogui.keyUp('a')
    # pyautogui.keyDown('d')
    # time.sleep(14)
    # pyautogui.keyUp('d')

    # pyautogui.keyDown('w')
    # b = round(random.uniform(0.1,0.2), 2)
    # time.sleep(b)
    # pyautogui.keyUp('w')
    # pyautogui.keyDown('w')
    # b = round(random.uniform(0.1,0.2), 2)
    # time.sleep(b)
    # pyautogui.keyUp('w')
    # pyautogui.keyDown('a')
    # b = round(random.uniform(13, 14), 2)
    # time.sleep(b)
    # pyautogui.keyUp('a')
    pyautogui.screenshot('file.png')
    img = Image.open('file.png')
    clickBiasa(966,933)
    while img.getpixel((1571,443))[0]!=74:
        print("Jalan")
        pyautogui.screenshot('file.png')
        img = Image.open('file.png')
        if img.getpixel((1571,443))[0]!=74:
            for i in hit:
                clickBiasa(i[0],i[1])
            pyautogui.keyDown('d')
            b = round(random.uniform(0.1, 0.13), 2)
            time.sleep(b)
            pyautogui.keyUp('d')
            time.sleep(1)
    
    pyautogui.keyDown('a')
    b = round(random.uniform(13, 14), 2)
    time.sleep(b)
    pyautogui.keyUp('a')
            

            
        
    
            

