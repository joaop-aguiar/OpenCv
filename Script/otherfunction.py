from time import sleep
import cv2
import imagesearch
import numpy as np
from ahk import AHK
import pyautogui
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

ahk = AHK


'''def enviar_mensagem():
    pyautogui.click(269, 755, button='left')
    pyautogui.click(36, 30, button='left')
    pyautogui.click(171, 310, button='left')
    pyautogui.typewrite('Ignora se der errado, estou fazendo alguns textes de programas', float(0.05))
    pyautogui.typewrite(['enter'])'''
    
#print(pyautogui.size())

alg = cv2.CascadeClassifier('C:/Users/User/Documents/Projetos/Clone/Haarcascade/haarcascade_frontalface_default.xml')

img = cv2.imread('C:/Users/User/Documents/Projetos/OpenCv/Script/imagens/amanda.png')
imagemcinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = alg.detectMultiScale(imagemcinza)
print(faces)

cv2.imshow('Faces', img)
cv2.waitKey(0)