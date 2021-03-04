from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from io import StringIO, BytesIO
import base64
import cv2
import numpy as np
import configparser
from cv import ImageManipulation

# intializing config parameters here:

Config = configparser.ConfigParser()
Config.read("config/default.ini")

app = Flask('edges')
CORS(app)


def cv_engine(img, operation):
    if operation == 'canny_edge':
        sigma = float(Config.get('canny', 'sigma'))
        im = ImageManipulation()
        canny = im.auto_canny(img_input=img, sigma=sigma)
        return canny
    elif operation == 'k-means-segmentation':
        print('kmm')
        num_of_clusters = int(Config.get('kmeans', 'num_of_clusters'))
        thresh = int(Config.get('kmeans', 'threshold'))
        im = ImageManipulation()
        kmm = im.kmeans_clustering(
            img_input=img, num_of_clusters=num_of_clusters, thresh=thresh)
        return kmm
    elif operation == 'watershed':
        thresh = int(Config.get('watershed', 'threshold'))
        im = ImageManipulation()
        dc = im.detect_corners(img_input=img, thr=thresh)
        return dc
    else:
        return None


def read_image(image_data):
    image_data = base64.decodebytes(image_data)
    with open('temp_image.jpg', 'wb') as f:
        f.write(image_data)
        f.close()
    img = cv2.imread('temp_image.jpg')
    return img


def encode_image(img):
    ret, data = cv2.imencode('.jpg', img)
    return base64.b64encode(data)

# This is the server to handle requests and get images from client


@app.route('/process_image', methods=['POST'])
def process_image():
    if not request.json or 'msg' not in request.json:
        return 'Server Error!', 500

    image_data = request.json['image_data'][23:].encode()
    operation = request.json['operation']
    print(operation)
    img = read_image(image_data)
    img_out = cv_engine(img, operation)
    image_data = encode_image(img_out)
    result = {'image_data': image_data, 'msg': 'Operation Completed'}
    return image_data, 200


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
