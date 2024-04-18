from rest_framework import serializers
from .models import Contact, Address, Mailid, mobile, Footer, Services, whatwedos, Menu, MenuItems, Gallery, About, AboutImage, Testimonials, Home, carousel, Homevideo, Homeservices, Homemenus, Homemenuimages,Homegallery, HomeImage, OurTeam

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'text']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street_address', 'city', 'state', 'postal_code','Door_No']

class MailidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailid
        fields = ['Mailid']

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = ['mobile']

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['Footer']

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['Icon', 'Heading', 'Description']

class WhatWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = whatwedos
        fields = ['Icon', 'Heading', 'Description']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Name']

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['Pdf']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['Image', 'Description']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['Description']

class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = ['Image']

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ['Name', 'Designation', 'kindofService', 'Testimonial']

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['Heading', 'Description']

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = carousel
        fields = ['Image']

class HomevideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homevideo
        fields = ['Video']

class HomeservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeservices
        fields = ['Description']

class HomemenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homemenus
        fields = ['Heading', 'Description']

class HomemenuimagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homemenuimages
        fields = ['Image']

class HomegallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Homegallery
        fields = ['Image', 'AlternativeImage']

class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImage
        fields = ['Image']

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['Name', 'Designation', 'Image']