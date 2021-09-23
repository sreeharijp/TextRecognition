!sudo apt install tesseract-ocr
!pip install pytesseract

import numpy
import cv2 as cv
from skimage import io
from google.colab.patches import cv2_imshow
import pytesseract
from PIL import Image
import os

url2="https://drive.google.com/uc?id=13GD5tXUUxOIJLteGCVfnxV2E-GwOSJ4m"
url="https://drive.google.com/uc?id=1aOa9FFt-IynLvu_0VZJfMTnneeZ4d2p8"
Img=io.imread(url)
#cv2_imshow(Img)
grey=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)
cv2_imshow(grey)
filename="{}.png".format(os.getpid())
cv.imwrite(filename,grey)
text=pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
