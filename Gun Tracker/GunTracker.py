import numpy as np
import cv2
import datetime
import imutils

gun_cascade = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in guns:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()

cv2.destroyAllWindows()



