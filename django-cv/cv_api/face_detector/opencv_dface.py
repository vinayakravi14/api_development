from django.conf import settings
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

def detect_face(path):

    img = cv2.imread(path)

    if type(img) is np.ndarray:
        img_temp = img.copy()
        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        face_url = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(
            base_path=os.path.abspath(os.path.dirname(__file__)))
        face_cascade = cv2.CascadeClassifier(face_url)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # region of interest
            roi_gray = gray[y: y+h, x: x+w]
            roi_color = img[y: y+h, x: x+w]

        print(img == img_temp)
        
        scale_percent = 60  # percent of original size


        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        plt.imshow(img)
        cv2.imwrite(path, img)

    else:
        print("Error!")
        print(path)
