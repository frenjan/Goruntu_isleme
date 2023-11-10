import cv2
from matplotlib import pyplot as plt

foto_gri = cv2.imread("beyaz_gul.jpg",0)


hist_gri = cv2.calcHist([foto_gri], [0],None,[256],[0,256])
plt.title("Gri Görüntü Histogram")
plt.figure(1)
plt.plot(hist_gri)
plt.show()


