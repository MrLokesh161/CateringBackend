from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class Address(models.Model):
    Door_No = models.CharField(max_length=20, null=True, blank=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} - {self.postal_code}"


class Mailid(models.Model):
    Mailid = models.EmailField()

class mobile(models.Model):
    mobile = models.BigIntegerField()

class Footer(models.Model):
    Footer = models.TextField()

class Services(models.Model):
    Icon = models.CharField(max_length=100)
    Heading = models.CharField(max_length=100)
    Description = models.TextField()

class whatwedos(models.Model):
    Icon = models.CharField(max_length=100)
    Heading = models.CharField(max_length=100)
    Description = models.TextField()

class Menu(models.Model):
    Name = models.CharField(max_length=100)

class MenuItems(models.Model):
    Pdf = models.FileField(upload_to='menu/')

class Gallery(models.Model):
    Image = models.ImageField(upload_to='gallery/')
    Description = models.CharField(max_length=100)

class About(models.Model):
    Description = models.TextField()

class AboutImage(models.Model):
    Image = models.ImageField(upload_to='about/')

class Testimonials(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    kindofService = models.TextField()
    Testimonial = models.TextField()

class Home(models.Model):
    Heading = models.CharField(max_length=100)
    Description = models.TextField()

class carousel(models.Model):
    Image = models.ImageField(upload_to='carousel/')

class Homevideo(models.Model):
    Video = models.URLField()

class Homeservices(models.Model):
    Description = models.TextField()

class Homemenus(models.Model):
    Heading = models.CharField(max_length=100)
    Description = models.TextField()

class Homemenuimages(models.Model):
    Image = models.ImageField(upload_to='homemenu/')

class Homegallery(models.Model):
    Image = models.ImageField(upload_to='homegallery/')
    AlternativeImage = models.ImageField(upload_to='homegalleryalt/')

class HomeImage(models.Model):
    Image = models.ImageField(upload_to='home/')

class OurTeam(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='team/')
