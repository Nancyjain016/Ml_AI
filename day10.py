import cv2
from time import sleep
import numpy as np

fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if flag:
       # Processing code
       img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       faces = fd.detectMultiScale(
           img_gray,
           scaleFactor=1.1,
           minNeighbors=5,
           minSize=(50,50)
       )
       np.random.seed(50)
       colors = np.random.randint(0,255, (len(faces),3)).tolist()
       i=0

       
       #th, img_bw = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
       for x,y,w,h in faces:
           cv2.rectangle(
               img, pt1=(x,y), pt2=(x+w,y+h), color=colors[i],thickness=2
           )
           i+=1
       # print(type(img_gray))
       # break

       cv2.imshow('Preview', img)
       key = cv2.waitKey(1)
       if key==ord('q'):
           break
    else:
        print('No Frames')
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()       