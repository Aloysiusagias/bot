import numpy as np
from PIL import ImageGrab, Image
import cv2
from numpy.core.defchararray import split
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def img_to_text(img):
    # img = Image.open('model.PNG')
    text = tess.image_to_string(img)
    # text = "\n".split(text)
    for x in text:
        c = x.isascii()
        if not c:
            text = penulis.replace(x, '')
    text = text[:-2]
    return text

while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,70,200,150)))
    teks = img_to_text(screen)
    print('|'+teks+'|')
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break