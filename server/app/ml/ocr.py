# Code inspired by https://github.com/makelove/OpenCV-Python-Tutorial/blob/master/my01-OCR%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB/Tessract-OCR/pytesseract/ocr.py
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import urllib.request
from dotenv import load_dotenv
from .nlp import cleanText
load_dotenv()
def getText(url, method="thresh"):
    try: 
        image_path = os.path.join(os.getenv('LOCAL_PATH'), 'test.png')
        urllib.request.urlretrieve(url, image_path)
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception:
        return ""
    if method == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove
    # noise
    elif method == "blur":
        gray = cv2.medianBlur(gray, 3)
    elif method == "gauss":
        gray = cv2.GaussianBlur(gray, (3,3), 255)
    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    text = cleanText(text)
    os.remove(filename)
    os.remove(image_path)
    return text[0:300]
