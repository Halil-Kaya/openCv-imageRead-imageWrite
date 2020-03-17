import cv2

img=cv2.imread("butterfly.jpg",0)

cv2.imshow("butte",img)


key=cv2.waitKey(0)

key=chr(key)

if key=='q':
    cv2.destroyAllWindows()
elif key=='s':
    cv2.imwrite("greyButterfly.jpg",img)
