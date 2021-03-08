# Django-CV API

## Overview
This project is a  implementation of Django-CV application which involves REST like features, where you can upload an image and choose a CV operation to be performed and it will be rendered in the API's host web-page. 

## Authors

- [Vinayak Ravi](https://github.com/vinayakravi14)

## Dependencies 

 You will need the following libraries and methods to prepare your environment 
```
numpy - pip3 install numpy
cv2 - pip3 install openv-python
scikit - pip3 install -U scikit-learn
matplotlib - pip3 install matplotlib
django - python -m pip install Django
```
For setting up Django projects follow this tutorial (https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

## Run Instructions

- Clone the repository 
```
git clone https://github.com/vinayakravi14/api_development.git
cd ~/django-cv/cv-api/
```

- Then launch the script file 
```
 python manage.py runserver 127.0.0.1:8000
```
- This launches a lightweight Django API hosting on 'http://127.0.0.1:8000/', (Note: you can host it pretty much on any URL.)
- The view and interactivity are done by two files. (Note: FLask likes it structured under the templates & static directories)
```
templates/first_view.html dface.html uimage.html
static/css/index.css
``` 
- Further, the user can navigate to the 'face_detector' by clicking on the 'CV techniques' in the navigation bar.  
- After which, the user can upload the image and click on 'detect image' to show an image with face-detected results. (to toggle the performance of the CV operation, tune parameters in 'opencv_dface.py')

## Debug if the API throws up an error or its unresponsive 

- Try clearing the cache/data from your browser and restart 
- Try ``` python manage.py makemigrations ``` and then `python manage.py migrate `, followed by the `python runserver` command 

## Example API window, after running the script
The Home window:
<img src="https://github.com/vinayakravi14/api_development/blob/main/django-cv/cv_api/sample_output/output.png" alt="sample_output"/>

The result: 
<img src="https://github.com/vinayakravi14/api_development/blob/main/django-cv/cv_api/sample_output/output.png" alt="sample_output"/>
