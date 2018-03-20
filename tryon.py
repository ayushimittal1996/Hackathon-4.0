import cv2
import numpy as np
from flask import render_template

x=0
y=0
w=0
h=0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Start Webcam (0 for inbuilt webam and 1 for external webcam)
def function(name):

    cap = cv2.VideoCapture(0)

    x_user = 0
    y_user = 0
    z_user = 0
    # Loop for each frame of webcame

    while cap.isOpened():
        ret,img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        print("hi")
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:

            s_img = cv2.imread(name)
            l_img = img
            x_onset = 3.2*w/s_img.shape[0]+ z_user
            y_onset = 2.5*h/s_img.shape[1]+z_user
            x_offset = int(x - x_onset*200)+x_user
            y_offset = int(y + h + 15)+y_user
            if x_offset<=0:
                xcut=abs(x_offset)
                x_offset=0
            else:
                xcut=0
            s_img = cv2.resize(s_img,(0,0),fx=x_onset,fy=y_onset)
            crop=s_img[0:l_img.shape[0]-y_offset,xcut:l_img.shape[1]-x_offset]
            #l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1]] = crop
            for c in range(0,3):
                l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1], c] = crop[:,:,c] * (crop[:,:,2]/255.0) +  l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1], c] * (1.0 - crop[:,:,2]/255.0)
           # cv2.putText(l_img,"a - Move left",(10,10),FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
            print("yes")
            cv2.imshow('img',l_img)
            cv2.imwrite("yes.jpeg",l_img)
            yield l_img
            k=cv2.waitKey(1)
            if k==97:
                x_user-=3
            elif k==100:
                x_user+=3
            elif k==119:
                y_user-=3
            elif k==115:
                y_user+=3
            elif k==122:
                z_user+=0.1
            elif k==120:
                z_user-=0.1
            if k==27:
                cap.release()
                cv2.destroyAllWindows()
