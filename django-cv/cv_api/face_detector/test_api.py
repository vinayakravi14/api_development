# import the necessary packages
import requests
import cv2
import json
import os
# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"
# # use our face detection API to find faces in images via image URL
# image = cv2.imread("obama.jpg")
# payload = {"url": "https://pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg"}
# r = requests.post(url, data=json.dumps(payload))
# print(r)
# # try:
# #     data = r.json()
# # except ValueError:
# #     print("Response content is not valid JSON")

# print ("obama.jpg: {}".format(r))
# # loop over the faces and draw them on the image
# for (startX, startY, endX, endY) in r["faces"]:
# 	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# # show the output image
# cv2.imshow("obama.jpg", image)
# cv2.waitKey(0)
# load our image and now use the face detection API to find faces in
# images by uploading an image directly
path = "/home/vinayak_ravi/Documents/git/api_development/django/cv_api/face_detector/test.jpg"
image = cv2.imread(path)


payload = {"image": open(path, "rb")}
# payload = dict(
#     image=open(path,"rb")
# )
r = requests.post(url, files=payload).json()

print("test.jpg: {}".format(r))
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# show the output image
cv2.namedWindow("test", cv2.WINDOW_GUI_EXPANDED)
imS = cv2.resize(image, (1000, 800))
cv2.imshow("test", imS)

cv2.waitKey(0)
