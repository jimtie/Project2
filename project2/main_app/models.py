from django.db import models

# Create your models here.
class Photo(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	image_link = models.URLField()
	

	def __str__(self):
		return self.name

# class User(models.Model):
# 	email = models.Email(max_length=200)
# 	password = models.

class Album(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	photos = models.ManyToManyField(Photo)

	def __str__(self):
		return self.name