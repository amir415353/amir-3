import cv2
import time
from mss import mss
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

time.sleep(5)
with mss() as sct:
    sct.shot()
img = cv2.imread("monitor-1.png")
y = 262
x = 93
h = 385
w = 384
crop_img = img[y:y+h, x:x+w]
cv2.imwrite(r'sc2.jpg', crop_img)
y = 182
x = 96
h = 29
w = 200
crop_img = img[y:y+h, x:x+w]
cv2.imwrite(r'index2.png', crop_img)
a = pytesseract.image_to_string(Image.open('index2.png'))
b = a.split()
print(b)
print(b[0])
