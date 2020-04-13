from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Album, Photo
# from .forms import AlbumForm, PhotoForm


# Define the home view
def home(request):
	return render(request, 'home.html')

def albums_index(request):
	albums = Album.objects.all()
	return render(request, 'albums.html', {'albums': albums})

def albums_detail(request,album_id):
	album = Album.objects.get(id=album_id)
	photos_album_doesnt_have = Album.objects.exclude(id__in = album.photos.all().values_list('id'))
	return render(request, 'albums/detail.html', {'album': album, 'photos': photos_album_doesnt_have})

def photos_index(request):
	photos = Photo.objects.all()
	return render(request, 'photos.html', {'photos': photos})

def photos_detail(request, photo_id):
	photo = Photo.objects.get(id=photo_id)
	return render(request, 'photos/detail.html', {'photo': photo})

def assoc_photo(request, album_id, photo_id):
  Album.objects.get(id=album_id).photos.add(photo_id)
  return redirect('photos_detail', album_id=album_id)
	

def album_createalbum(request):
	form = AlbumForm(request,POST)
	if form.is_valid():
		new_album = form.save(commit = False)
		new_album_id = album_id
		new_album.save()
	return redirect('albums', album_id = album_id)

def photo_createphoto(request):
	form = PhotoForm(request,POST)
	if form.is_valid():
		new_photo = form.save(commit = False)
		new_photo_id = photo_id
		new_photo.save()
	return redirect('photos', photo_id = photo_id)