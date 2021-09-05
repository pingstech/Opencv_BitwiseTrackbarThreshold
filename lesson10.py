import cv2

img=cv2.imread("sudoku.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive_Threshold1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
adaptive_Threshold2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Original Image",img)
cv2.imshow("Adaptive Threshold Mean Image",adaptive_Threshold1)
cv2.imshow("Adaptive Threshold Gaussian Image",adaptive_Threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()