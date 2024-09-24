import sys

import cv2

img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("File Error")

# TODO: Color to grayscale, I = round(0.299*R + 0.587*F + 0.114*B)

cvt_img = img
cv2.imshow(cvt_img)
