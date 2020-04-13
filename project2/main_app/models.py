from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	image_link = models.URLField()


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("photo_detail", kwargs={'pk': self.id})

# class User(models.Model):
# 	email = models.Email(max_length=200)
# 	password = models.

class Album(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	photos = models.ManyToManyField(Photo)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

