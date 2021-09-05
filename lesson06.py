import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)                             # Burada 0'lardan oluşan bir matris oluşturduk.
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)     # Buradaysa matrisin belirtilen koordinatlarına beyaz ve içi dolu olan bir kare yerleştirdik
img2=np.zeros((250,500,3),np.uint8)                             # Yine aynı şekilde 0'lardan oluşan bir matris oluşturduk.
img2=cv2.rectangle(img2,(250,0),(500,500),(255,255,255),-1)     # Bu sefer ise yarısını beyaz, yarısını ise siyah olan bir görüntü oluşturduk
#cv2.imwrite("Image1.jpg",img1)                                 # Matrislerle oluşturduğumuz görüntüleri kaydettik
#cv2.imwrite("Image2.jpg",img2)

#**************************************  BU İŞLEMLERİ GÖRÜNTÜ ÜSTÜNDE MASKELEME YAPACAĞIMIZ ZAMAN KULLANACAĞIZ BU YÜZDEN ÖNEMLİ  **************************************

bitAND=cv2.bitwise_and(img2,img1)                 # İki resim arasında klasik VE işlemini yaptık
bitOR=cv2.bitwise_or(img2,img1)                   # İki resim arasında klasik VEYA işlemini yaptık
bitXOR=cv2.bitwise_xor(img2,img1)                 # İki resim arasında klasik VEYA DEĞİL işlemini yaptık
bitNOT1=cv2.bitwise_not(img2,img1)                # İki resim arasında klasik DEĞİL işlemini yaptık   
bitNOT2=cv2.bitwise_not(img1,img2)                # İki resim arasında klasik DEĞİL işlemini yaptık

#**********************************************************************************************************************************************************************

cv2.imshow("Picture 1 ",img1)
cv2.imshow("Picture 2 ",img2)
cv2.imshow("BITWISE AND",bitAND)
cv2.imshow("BITWISE OR",bitOR)
cv2.imshow("BITWISE XOR",bitXOR)
cv2.imshow("BITWISE NOT-1",bitNOT1)
cv2.imshow("BITWISE NOT-2",bitNOT2)
cv2.waitKey(0)
cv2.destroyAllWindows()