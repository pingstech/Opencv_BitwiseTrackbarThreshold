import cv2
import numpy as np

def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Image")                            # Trackbar için pencere oluşturduk
cv2.createTrackbar("B","Image",0,255,nothing)       # "B" isminde bir çubuk oluşturduk ve 0 ile 255 değer aralığında oluşturduk, ayrıca anlık değeri de "nothing" isimli fonksiyona göndererek ekrana bastık
cv2.createTrackbar("G","Image",0,255,nothing)       # "G" isminde bir çubuk oluşturduk ve 0 ile 255 değer aralığında oluşturduk, ayrıca anlık değeri de "nothing" isimli fonksiyona göndererek ekrana bastık
cv2.createTrackbar("R","Image",0,255,nothing)       # "R" isminde bir çubuk oluşturduk ve 0 ile 255 değer aralığında oluşturduk, ayrıca anlık değeri de "nothing" isimli fonksiyona göndererek ekrana bastık
switch='OFF / ON'
cv2.createTrackbar(switch,"Image",0,1,nothing)


while True:
    cv2.imshow("Image",img)
    b_Value=cv2.getTrackbarPos("B","Image")         # Trackbarda olan "B" çubuğunun anlık değerini "b_Value" isimli değişkene atadık
    g_Value=cv2.getTrackbarPos("G","Image")         # Trackbarda olan "G" çubuğunun anlık değerini "g_Value" isimli değişkene atadık
    r_Value=cv2.getTrackbarPos("R","Image")         # Trackbarda olan "R" çubuğunun anlık değerini "r_Value" isimli değişkene atadık
    switchPos=cv2.getTrackbarPos(switch,"Image")    # Trackbarda olan "switch" çubuğunun anlık değerini "switchPos" isimli değişkene atadık
    
    if switchPos == 1:
        img[:]=[b_Value,g_Value,r_Value]            # Buradaysa oluşturduğumuz tüm matrisi trackbardan aldığımız değerlere göre değiştiriyoruz
    else:
        img[:]=[0]

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()