import csv
import pandas as pd
import json
import pandas as pd
import sys
import trace
import threading
import time
from growtopiaBFG import bfg
import telegram
from constans import API_KEY
import pyautogui

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False
 
    def start(self):
        self.__run_backup = self.run
        self.run = self.__run     
        threading.Thread.start(self)
 
    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup
 
    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None
    
    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace
    
    def kill(self):
        self.killed = True

def do_something():
    for i in range(20):
        time.sleep(1)
        print(i,"a")

# t1 = threading.Thread(target=do_something, args =(lambda : stopp, ))
threads = []
bot = telegram.Bot(API_KEY)
def respons(input_text):
    text = input_text["message"]["text"]
    print(text)
    if(text == "mulai"):
        t1 = thread_with_trace(target = bfg)
        threads.append(t1)
        for thread in threads:
            print(thread.is_alive())
            if not thread.is_alive():
                try :
                    thread.start()
                except:
                    print("lanjut")

    if(text == "stop"):
        for thread in threads:
            thread.kill()
            thread.join()
    
    if(text == "ss"):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'D:\Latihan\Bot\pyautogui\bot growtopia\ss.png')
        bot.send_photo(input_text["message"]["chat_id"],photo=open('ss.png', 'rb'))