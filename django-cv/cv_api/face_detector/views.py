from django.shortcuts import render
from .forms import UploadImageForm, ImageUploadModel
# from .forms import BinarizeForm, StreamForm, CaptureForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .opencv_dface import detect_face
# from .crop_image import crop_image
# from .subtract import subtract
# from .binarize_mask import binarize_mask
# from .stream_video import stream_video
# from .capture_image import capture_image
from django.http import HttpResponseRedirect
# Create your views here.


def first_view(request):
    return render(request, 'first_view.html', {})


def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            upload_file_url = fs.url(filename)
            return render(request, 'uimage.html',
                          {'form': form, 'upload_file_url': upload_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'uimage.html',
                      {'form': form})


def dface(request):
    if request.method == 'POST':
        form = ImageUploadModel(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            detect_face(settings.MEDIA_ROOT_URL + imageURL)
            return render(request, 'dface.html',
                          {'form': form, 'post': post})
    else:
        form = ImageUploadModel()

        return render(request, 'dface.html',
                      {'form': form})
