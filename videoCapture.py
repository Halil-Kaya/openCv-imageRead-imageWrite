import cv2

video=cv2.VideoCapture("vtest.avi")


while True:
    deger , frame = video.read()#deger-> true or false donuyor ici dolu mu diye kontrol
    print(deger)
    if deger==True:
        cv2.imshow("ds",frame)
        if cv2.waitKey(20) & 0xFF==ord("q"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()