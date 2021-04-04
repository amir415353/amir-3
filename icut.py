import pyautogui
import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'F:\Program Files\ocr\tesseract.exe'
img = cv2.imread("index.png")
y = 264
x = 84
h = 483
w = 482
crop_img = img[y:y+h, x:x+w]
cv2.imwrite(r'sc2.jpg', crop_img)
y = 167
x = 84
h = 42
w = 482
crop_img = img[y:y+h, x:x+w]
cv2.imwrite(r'index2.png', crop_img)
a = pytesseract.image_to_string(Image.open('index2.png'))
b = a.split()
print(b)
print(b[0])
exit()

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'sc.jpg')
