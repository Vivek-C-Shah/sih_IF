import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

UPLOADS_FOLDER = 'uploads/'
IMAGE_FILENAME = 'test.png'
IMAGE_PATH = os.path.join(UPLOADS_FOLDER, IMAGE_FILENAME)

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result

words = []
result_string = ""

for detection in result:
    words.append(detection[1])
    print(detection[1])
    result_string = ' '.join(words)
print("test: ")

print(result_string)
