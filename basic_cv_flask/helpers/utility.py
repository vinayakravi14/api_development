import os
import cv2


def import_data(path, type: str):
    img = cv2.imread(path)

    if type == 'rgb':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if type == 'gray':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
