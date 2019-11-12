import numpy as np 
import cv2 
import time 
import socket 
from imutils.video import VideoStream
 
 
HOST = "" 
PORT = 8080 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
s.bind((HOST,PORT))
print("Socket bind complete")
 
s.listen(1) 
print("Socket now listening")
 
conn,addr = s.accept();
print("Socket Connected by : ", addr)

cascade = cv2.CascadeClassifier('haarcascade.xml')
cap  = VideoStream(usePiCamera=True).start()
time.sleep(2.0)


while True:
        img = cv2.flip(img,-1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray,1.3,5)


        for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]

        cv2.imshow('video', img)


        if len(faces) > 0: 
                print(len(faces)) 
                res = len(faces) 
                res = str(res)
                conn.sendall(res.encode("utf-8"))

        k = cv2.waitKey(30) 
        if k==27:
                break

cap.release() 
cv2.destoryAllWindows() 
conn.close() 
s.close()
