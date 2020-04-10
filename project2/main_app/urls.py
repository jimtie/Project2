from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('albums/', views.albums_index, name='album_index'),
	path('photos/', views.photos_index, name='photo_index'),
	path('albums/<int:album_id>/', views.albums_detail, name='albums_detail'),
	path('photos/<int:photo_id>/', views.photos_detail, name='photos_detail'),
	path('album/createalbum/', views.album_createalbum, name='createalbum'),
]