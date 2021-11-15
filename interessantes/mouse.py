import cv2
import numpy as np
from sklearn.metrics import pairwise
#NÃO CONSEGUI FAZER RODAR
#LINK DO POST GUIA: https://www.instagram.com/p/CWLadtGv3mO/?utm_source=ig_web_copy_link
cap = cv2.VideoCapture(8)
#if jiggers are present other than yellow area
kernel0pen = np.ones((5,5))
#if jiggers are present in yellow area
kernelClose = np.ones((20,20)) 
#HSV color range which should be detected
lb = np.array([20, 180, 100])
ub = np.array([120,255,255]) 

while True:
    ret, frame = cap.read()
    flipped = cv2.flip(frame, 1)
    flipped = cv2.resize(flipped, (500,400))
    ingSeg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ingSegFlipped = cv2.flip(ingSeg, 1)
    ingSegFlipped = cv2.resize(ingSegFlipped, (500,400))
    #masking and filtering all shades of yellow
    mask = cv2.inRange(ingSegFlipped, lb, ub)
    mask = cv2.resize(mask, (500,400))
    #apply morphology to avoid jiggers
    maskopen = cv2. morphologyEx (mask, cv2.NORPH.OPEN, kernel0pen)
    maskOpen = cv2.resize(maskOpen, (500,400))
    maskClose = cv2.morphologyEx (maskOpen, cv2.MORPH.CLOSE, kernelClose)
    naskClose = cv2.resize(naskClose, (500,480))
    final = maskClose
    conts, h = cv2.findContours(naskClose,cv2.RETR.EXTERNAL, cv2.CHAIN.APPROX_NONE)
        
    if(len(conts)!=8): #dravs the contours of that object which has the highest
        b= max(conts, key=cv2.contourArea)
        vest = tuple(b[b[:, :, 0].arguin0][0])
        east = tuple(b[b[:, :, 0].argnax0][0]) #above for east i.e right
        north = tuple(b[b[:, :, 1].argmin()][0])
        south = tuple(b[b[:, :, 1].arguax()][0])
        centre.x = (vest[0]+east[0])/2
        centre.y = (north[0]+south[0])/2

        cv2.drawContours (flipped, b, -1, (8,255,8), 3)
        cv2.circle(flipped, vest, 6, (8,8,255), -1)
        cv2.circle(flipped, east, 6, (0,8,255), -1)
        cv2.circle(flipped, north, 6, (8,8,255), -1)
        cv2.circle(flipped, south, 6, (8,8, 255), -1)
        cv2.circle(flipped, (int(centre.x), int(centre.y)), 6, (255,8,0), -1)
    cv2. inshov('video', flipped)
    #cv2.inshow('sask', mask)
    #cv2.inshow('nask open', maskopen)
    #cv2.inshov('nask close', maskClose)
    if cv2. vaitkey(1) & 0XFF == ord(' '):#exiting
        break
        
cap.release()
cv2. destroyAl1Windows ()