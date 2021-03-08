# basic_cv_flask

## Overview
This project is a basic flask implementation of CV application which involves using GET/POST and REST like features. You can upload an image and choose a CV operation to be performed and it will be rendered in the API's host page. 

## Authors

- [Vinayak Ravi](https://github.com/vinayakravi14)

## Dependencies 

 You will need the following libraries and methods to prepare your environment 
```
numpy - pip3 install numpy
cv2 - pip3 install openv-python
scikit - pip3 install -U scikit-learn
matplotlib - pip3 install matplotlib
flask - pip3 install Flask 
```


## Run Instructions

- Clone the repository 
```
git clone https://github.com/vinayakravi14/api_development.git
cd ~/basic_cv_flask
```

- Then launch the script file 
```
python3 app.py
```
- This launches a lightweight API hosting on 'http://127.0.0.1:5000/', (Note: you can host it pretty much on any URL.)
- The view and interactivity are done by two files. (Note: FLask likes it structured under the templates & static directories)
```
templates/index.html
static/index.js
``` 
- Further, the user can load in the image on the hosted site and click, 'Load image' and  choose the necessary operation and then click on 'process image' to view the processed result on the window. 
- The 'process image' is taken care by the 'cv_engine' in 'app.py', which takes in different methods from 'cv.py' (to perform the CV operations)
```
cv.py
(consists of 3 CV operations kmeans segmentation, watershed segmentation, canny-edge detection), modify to fit any application which returns an (ndarray) image)
```
- You can alter the operation's performance by tuning the parameters in 'config/default.ini' and you might need to stop and re-launch the app, if it dosent work straight away. (Note: you can alter and include parameters by changing it in the cv.py, app.py and default.ini correspondingly.)

```
config/default.ini

#### contains ######
[kmeans]
num_of_clusters = 4
threshold = 180

[canny]
sigma = 10

[watershed]
threshold = 10
#####################
```


## Example API window, after running the script


<img src="https://github.com/vinayakravi14/api_development/blob/main/basic_cv_flask/sample_output/sample.png" alt="sample_output"/>
