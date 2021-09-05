import cv2
import numpy as np

def nothing(temp):
    print("Value: ",temp)

cap=cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,1024)

cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper Saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper Value", "Tracking", 0, 255, nothing)


while True:
    _,frame=cap.read()
    #frame=cv2.imread("smarties.png")
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowHue=cv2.getTrackbarPos("Lower Hue","Tracking")
    uppHue=cv2.getTrackbarPos("Upper Hue","Tracking")
    lowSat=cv2.getTrackbarPos("Lower Saturation","Tracking")
    uppSat=cv2.getTrackbarPos("Upper Saturation","Tracking")
    lowVal=cv2.getTrackbarPos("Lower Value","Tracking")
    uppVal=cv2.getTrackbarPos("Upper Value","Tracking")

    lowerVal_Blue=np.array([lowHue,lowSat,lowVal])
    upperVal_Blue=np.array([uppHue,uppSat,uppVal])

    mask=cv2.inRange(hsv,lowerVal_Blue,upperVal_Blue)
    res_Img=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Original Image",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("After Bitwise",res_Img)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()