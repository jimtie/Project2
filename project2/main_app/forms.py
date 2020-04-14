from django.forms import ModelForm
from .models import Album, Photo
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class AlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['name', 'description']

class PhotoForm(ModelForm):
	class Meta:
		model = Photo
		fields = ['name', 'description', 'image_link']

# class AlbumOptForm(ModelForm):
# 	"""docstring for AlbumOptForm"""
# 	class Meta:
#         model = AlbumOpt
#         fields = ['name']
		
# class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']