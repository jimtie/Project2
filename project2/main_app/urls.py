from django.urls import path
from . import views


# app_name = 'accounts'

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('albums/', views.albums_index, name='album_index'),
	path('photos/', views.photos_index, name='photo_index'),
	path('albums/<int:album_id>/', views.albums_detail, name='albums_detail'),
	path('photos/<int:photo_id>/', views.photos_detail, name='photos_detail'),
	path('album/createalbum/', views.album_createalbum, name='album_createalbum'),
	path('albums/<int:album_id>/assoc_photo/<int:photo_id>/', views.assoc_photo, name='assoc_photo'),
	path('albums/<int:album_id>/<int:photo_id>', views.photos_detail, name='photos_detail'),
	path('photo/', views.PhotoList.as_view(), name='photo_index'),
    path('photo/<int:pk>/', views.PhotoDetail.as_view(), name='photo_detail'),
    path('photo/create/', views.PhotoCreate.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
    path('accounts/signup', views.signup, name='signup'),

    # path('signup/', views.SignUpView.as_view(), name='signup')
]