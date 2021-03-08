from django import forms
from .models import ImageUploadModel


class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()


class ImageUploadModel(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document')
