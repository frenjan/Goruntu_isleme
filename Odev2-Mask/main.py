import cv2
from matplotlib import pyplot as plot
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ret,vid=cam.read()
    hsv=cv2.cvtColor(vid,cv2.COLOR_BGR2HSV) # rgb'yi hsv'ye çevirme
    alt=np.array([0,100,100]) #kırmızı renk alt sınırı
    ust=np.array([10,255,255]) #kırmızı renk üst sınırı
    kirmizi=cv2.inRange(hsv,alt,ust) #bizim videoda verdiğimiz renk aralığı içindeki renkleri beyaz diğerlerini siyah yapar
    arkaplan=cv2.bitwise_and(vid,vid,mask=kirmizi) #verdiğimiz renk harici diğer renkler gözükmez

    cv2.imshow("beyaz",kirmizi)
    cv2.imshow("normal",vid)
    cv2.imshow("kirmizi",arkaplan)

    if cv2.waitKey(30) & 0xFF==ord("x"): # x'e basınca kapanır
        break

cam.release()
cv2.destroyAllWindows()


