from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Define the home view
def home(request):
	return render(request, 'home.html')

def albums_index(request):
	albums = Album.objects.all()
	return render(request, 'albums.html', {'albums': albums})

def albums_detail(request,album_id):
	album = Album.objects.get(id=album_id)
	photos_album_doesnt_have = Photo.objects.exclude(id__in = album.photos.all().values_list('id'))
	print (photos_album_doesnt_have)
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
	

# def album_createalbum(request):
# 	# if request.method == 'POST':
# 	form = AlbumForm(request,POST)
# 	if form.is_valid():
# 		new_album = form.save(commit = False)
# 		new_album_id = album_id
# 		new_album.save()
# 	return redirect('albums', album_id = album_id)

def album_createalbum(request):
    # If a post request is made to this view function
    if request.method == 'POST':
        # We save the form data to a new variable
        form = AlbumForm(request.POST)
        # We make sure the data passes validations
        if form.is_valid():
            # If it does, associate album with logged in user and 
            # save it in the database
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            # Redirect the user to the new album's detail page
            return redirect('albums_detail', album.id)
    else:
        # If it's a get request, load the form from forms.py
        form = AlbumForm()
    # Save the form to a new variable
    context = { 'form': form }
    # Render the album form template with the form
    return render(request, 'albums/album_form.html', context)

def photo_createphoto(request):
	form = PhotoForm(request,POST)
	if form.is_valid():
		new_photo = form.save(commit = False)
		new_photo_id = photo_id
		new_photo.save()
	return redirect('photos', photo_id = photo_id)


class PhotoList(ListView):
    model = Photo

class PhotoDetail(DetailView):
    model = Photo

class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['name', 'description']

class PhotoDelete(DeleteView):
    model = Photo
    success_url = '/photo/'










