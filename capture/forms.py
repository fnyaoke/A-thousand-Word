from django.forms import ModelForm
from django.forms.widgets import FileInput
from .models import Image
from cloudinary.forms import CloudinaryFileField

# class PhotoForm(ModelForm):
#   class Meta:
#       model = Image
#       fields = '__all__'

class PhotoForm(ModelForm):
      class Meta:
        model = Image
        fields = '__all__'
        image = CloudinaryFileField(
        # attrs = { 'style': "margin-top: 30px" },
        options = {
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 1000, 'height': 1000,
            'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
        })