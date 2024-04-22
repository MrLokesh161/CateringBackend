from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class HomeImage(models.Model):
    Image = models.ImageField(upload_to='HomeImage/')

class HomeAbout(models.Model):
    Image = models.ImageField(upload_to='HomeAbout/')

class HomeGallery(models.Model):
    Image = models.ImageField(upload_to='HomeGallery/')
    AlternateImage = models.ImageField(upload_to='HomeGallery/')

class Gallery(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Gallery/')

class HomeFoods(models.Model):
    Image = models.ImageField(upload_to='HomeFoods/')
