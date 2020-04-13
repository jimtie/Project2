from django.forms import ModelForm
from .models import Album, Photo
class AlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['name', 'description']

class PhotoForm(ModelForm):
	class Meta:
		model = Photo
		fields = ['name', 'description', 'image_link']