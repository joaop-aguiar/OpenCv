from time import sleep
import cv2
import imagesearch
import numpy as np
from ahk import AHK
import pyautogui
import pytesseract
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

ahk = AHK

img1 = cv2.imread('C:/Users/User/Documents/Projetos/OpenCv/Script/imagens/text.png') 
img2 = cv2.imread('C:/Users/User/Documents/Projetos/OpenCv/Script/imagens/opencv logo.png')

dst = cv2.addWeighted(img1, 0,7, img2, 1,3,0)

cv2.imshow('dst', dst) 
cv2.waitKey(0) 
cv2.destroyAllWindows(0)










































'''def enviar_mensagem():
    pyautogui.click(269, 755, button='left')
    pyautogui.click(36, 30, button='left')
    pyautogui.click(171, 310, button='left')
    pyautogui.typewrite('Ignora se der errado, estou fazendo alguns textes de programas', float(0.05))
    pyautogui.typewrite(['enter'])'''
    

