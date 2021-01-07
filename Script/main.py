import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('D:/OpenCV/opencv/Script/text.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#detecção de letras
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data('D:/OpenCV/opencv/Script/text.png')
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,0),2)
            cv2.putText(img,b[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

#detecção de números
'''hImg,wImg,_ = img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data('D:/OpenCV/opencv/Script/text.png', config=cong)
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,0),2)
            cv2.putText(img,b[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)'''


    

cv2.imshow('Result',img)
cv2.waitKey(0)
