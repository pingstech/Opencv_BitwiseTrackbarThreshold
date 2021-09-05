import cv2
img=cv2.imread("gradient.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)      # cv2.threshold(x,threshold,threshold max değeri,threshold type)
                                                        # BURADA EĞER GÖRESELDE 127 DEĞERİNDEN KÜÇÜK OLANAR 0 OLARAK BÜYÜK OLANLAR İSE 1 OLARAK
                                                        # YENİDEN DEĞERLENDİRİLİR. EĞER ATANAN BU DEĞERLER 0 İSE SİYAH, 1 İSE BEYAZ OLARAK GÖRÜRÜZ

_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)  # BURADA İSE TERSİNİ ALDIK

_,th3=cv2.threshold(img,255,255,cv2.THRESH_TRUNC)       # İLK PARAMETRE DEĞERİ NE KADAR AZALIRSA O KADAR ÇOK 0'A YAKLAŞIYOR(YANİ SİYAH OLUYOR)

_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)      # İKİNCİ PARAMETRE DEĞERİMİZ, BİZİM THRESHOLD DEĞERİMİZDEN YANİ İLK PARAMETRE DEĞERİNDEN
                                                        # AZ OLDUĞUNDA 0 DEĞERİNİ ALIR. EĞER BÜYÜKSE DEĞERİNİ KORUR

_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)  # BURADA İSE TERSİNİ ALDIK

cv2.imshow("Original Image",img)
cv2.imshow("Binary Thresholded Image",th1)
cv2.imshow("Inverse Binary Thresholded Image",th2)
cv2.imshow("Trunc Thresholded Image",th3)
cv2.imshow("To Zero Thresholded Image",th4)
cv2.imshow("Inverse To Zero Thresholded Image",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()