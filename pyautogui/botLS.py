import ctypes
from PIL.ImageOps import grayscale
import pyautogui
import win32api, win32con
import time
import keyboard
from PIL import Image
import ctypes
import pydirectinput

def click(x,y):
    print('jalan1')
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(1)
    # pyautogui.click(x, y, button='left')
    # win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    # time.sleep(0.1)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    # pydirectinput.click()
    time.sleep(1)

def space():
    print('Pencet spasi')
    # pyautogui.keyDown('space')
    # time.sleep(1)
    # pyautogui.keyUp('space')
    print('sebelum',keyboard.is_pressed('space'))
    keyboard.send("space")
    print('sesudah',keyboard.is_pressed('space'))


time.sleep(3)

korx = 1116
kory = 747
Rrr = 37

while keyboard.is_pressed('q') == False:
    print('jalan2')
    pyautogui.screenshot('file.png')
    img = Image.open('file.png')
    coba = 0
    coba2 = 0
    terima = False
    while(coba <= 5):
        eventt = pyautogui.locateCenterOnScreen('lvlupfishing.png', confidence=0.8)
        if(eventt != None):
            print('masuk lvlup')
            x, y = eventt
            click(int(x), int(y))
            coba = 6
            terima = True
        else :
            coba += 1
    
    coba = 0

    while(coba <= 5):
        eventt = pyautogui.locateCenterOnScreen('inventory - hadiah.png', confidence=0.8)
        if(eventt != None):
            print('Masuk inventory - hadiah')
            x, y = eventt
            click(int(x), int(y))
            coba = 6
            while(coba2 <= 10):
                xi = pyautogui.locateCenterOnScreen('x inven.png', confidence=0.8)
                if(xi != None):
                    time.sleep(2)
                    print('Masuk x')
                    x, y = xi
                    click(int(x), int(y))
                    coba2 = 11
                    terima = True
                else:
                    coba2+=1
        else :
            coba += 1
    
    coba = 0

    if(img.getpixel((korx,kory))[0]!=Rrr):
        print('jalan3')
        while(coba <= 5):
            terima1 = pyautogui.locateCenterOnScreen('terima event 1.png', confidence=0.8)
            terima2 = pyautogui.locateCenterOnScreen('terima event 2.png', confidence=0.8)
            if(terima1 != None or terima2 != None):
                print('Masuk terima')
                sudah = False
                while not sudah:
                    if(terima1 != None):
                        print('Masuk terima 1')
                        x, y = terima1
                        click(int(x), int(y))
                        terima = True
                    elif(terima2 != None):
                        print('Masuk terima 2')
                        x, y = terima2
                        click(int(x), int(y))
                        space()
                        terima = True
                    if(terima):
                        time.sleep(2)
                        print('Masuk teriimaaa')
                        while(coba2 <= 10):
                            selesai = pyautogui.locateCenterOnScreen('selesai event.png', confidence=0.8)
                            if(selesai != None):
                                print('Masuk selesai')
                                x, y = selesai
                                time.sleep(1)
                                click(int(x), int(y))
                                time.sleep(2)
                                terima = False
                                coba2 = 11
                                coba = 6
                                sudah = True
                            else :
                                coba2 += 1
                    else :
                        print('tidak masuuk teriimaa')
            else:
                coba+=1



        if(not terima):
            click(korx,kory)
            ketemu = False
            while not ketemu:
                jual = pyautogui.locateCenterOnScreen('jual.png', confidence=0.8)
                if jual != None:
                    x,y = jual
                    print('masuk jual')
                    click(int(x), int(y))
                    ketemu = True
                    tutup = False
                    time.sleep(2)
                    while not tutup:
                        tp = pyautogui.locateCenterOnScreen('tutup pancing 2.png', confidence=0.8)
                        if tp != None:
                            x, y = tp
                            print('masuk tutup')
                            click(int(x), int(y))
                            tutup = True
                            time.sleep(1)
            
        else :
            print('tidak ketemu')
    else :
        print('kosong')
    time.sleep(2)