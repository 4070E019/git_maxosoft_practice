import cv2
import numpy as np


# 載入分類器
#face_cascade.load('C:/anaconda3/envs/Ruby/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#載入影像
cap = cv2.VideoCapture(0)
print(cv2.data.haarcascades)
while True:
    _, img = cap.read()
    #轉化成灰階圖片    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #偵測臉部   
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #畫框
    for (x, y, w, h) in faces:#臉
        cv2.rectangle (img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img [y:y+h, x:x+w]
       
        
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
    cv2.imshow('img', img)                     #秀出圖片
    if cv2.waitKey(30)== ord('x'):
           break
     
    #cv2.imwrite( "result.jpg", img )           #保存圖片
cap.release()                             #等待按下任一按鍵
cv2.destroyAllWindows()                    #關閉視窗     



