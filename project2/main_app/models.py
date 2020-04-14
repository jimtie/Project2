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
# 	name = models.CharField(max_length=200)
# 	password = models.CharField(max_length=100)
# 	photos = models.ManyToManyField(Photo)
# 	# albums = models.ForeignKey()

# 	def __str__(self):
# 		return self.name

class Album(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	photos = models.ManyToManyField(Photo)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name



# class AlbumOpt(models.Model):
#     # providing a string in the field params changes the 
#     # label in Django admin and on generated model forms
#     name = models.CharField(max_length=100)
    
    # meal = models.CharField(
    #     max_length=1,
    #     # add the choices option and provide the MEALS as the value
    #     choices=MEALS,
    #     # set the default meal to Breakfast
    #     default=MEALS[0][0]
    # )
    # cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    # # overwrite the __str__ to improve shell experience
    # def __str__(self):
    #     return f"{self.get_meal_display()} on {self.date}"
    # class Meta:
    #     ordering = ['-date']
