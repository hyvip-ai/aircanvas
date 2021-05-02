import cv2
import numpy as np
cv2.namedWindow("Trackbars")
paintwindow = np.ones((480,640,3),np.uint8)
paintwindow[:,:,:]=255
def exit(a):
    pass
cv2.createTrackbar("h_min","Trackbars",93,179,exit);
cv2.createTrackbar("h_max","Trackbars",119,179,exit);
cv2.createTrackbar("s_min","Trackbars",92,255,exit);
cv2.createTrackbar("s_max","Trackbars",255,255,exit);
cv2.createTrackbar("v_min","Trackbars",183,255,exit);
cv2.createTrackbar("v_max","Trackbars",255,255,exit);
capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def getcolor(img):
    hmin=cv2.getTrackbarPos("h_min","Trackbars")
    hmax=cv2.getTrackbarPos("h_max","Trackbars")
    smin=cv2.getTrackbarPos("s_min","Trackbars")
    smax=cv2.getTrackbarPos("s_max","Trackbars")
    vmin=cv2.getTrackbarPos("v_min","Trackbars")
    vmax=cv2.getTrackbarPos("v_max","Trackbars")
    lower = np.array([hmin,smin,vmin]);
    upper = np.array([hmax,smax,vmax]);
    mask = cv2.inRange(img,lower,upper)
    return mask
colors=[(255,0,0),(14,16,82),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
colorindex = 0
while True:
    cv2.rectangle(paintwindow, (0, 0), (80, 65), (0, 0, 0), 3)
    cv2.rectangle(paintwindow, (80, 0), (160, 65), colors[0],  cv2.FILLED)
    cv2.rectangle(paintwindow, (160, 0), (240, 65), colors[1], cv2.FILLED)
    cv2.rectangle(paintwindow, (240, 0), (320, 65), colors[2], cv2.FILLED)
    cv2.rectangle(paintwindow, (320, 0), (400, 65), colors[3], cv2.FILLED)
    cv2.rectangle(paintwindow, (400, 0), (480, 65), colors[4], cv2.FILLED)
    cv2.rectangle(paintwindow, (480, 0), (560, 65), colors[5], cv2.FILLED)
    cv2.rectangle(paintwindow, (560, 0), (640, 65), colors[6], cv2.FILLED)
    success,img = capture.read()
    hue = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = getcolor(hue);
    contours, histeria = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
    for cnt in contours:

        ((x,y),radius) = cv2.minEnclosingCircle(cnt)
        x = int(x)
        y = int(y)

        radius = int(radius)
        # print(x,y,radius)
        cv2.circle(img,(x,y),radius,colors[colorindex],3)
        cv2.circle(paintwindow,(x,y),radius,colors[colorindex],cv2.FILLED)

        if y<65:

            if x<80:
                paintwindow[:,:,:]=255
            elif x<160:
                colorindex=0
            elif x<240:
                colorindex=1

            elif x<320:
                colorindex=2

            elif x<400:
                colorindex=3

            elif x<480:
                colorindex=4

            elif x<560:
                colorindex=5

            elif x<640:
                colorindex=6
    cv2.imshow("Main",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Paint",paintwindow)
    if cv2.waitKey(1)& 0xFF == ord("q"):
        break