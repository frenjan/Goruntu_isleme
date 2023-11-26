import cv2


cam=cv2.VideoCapture("http://192.168.31.46:8080/video") #telefon kamerası ip adresi

while cam.isOpened():
    ret,kamera=cam.read()

    cv2.imshow("Video",kamera)
    gray = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (11, 11), 0)

    canny = cv2.Canny(blur, 30, 150, 3)
    dilated = cv2.dilate(canny, (1, 1), iterations=0)

    cv2.imshow("kenar_bulucu",dilated)
    (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(kamera, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

    print("Prinç Sayısı : ", len(cnt))

    if cv2.waitKey(1)==ord("x"):
        break

cv2.destroyAllWindows()