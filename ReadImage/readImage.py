import cv2

img= cv2.imread("cat.png",0) ##siyah beyaz anlamına geliyor

cv2.imshow("First Image",img)

print(img.size)

k =cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("cat_copy.png",img)
    cv2.destroyAllWindows()