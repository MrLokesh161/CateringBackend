from rest_framework import serializers
from .models import Contact, HomeImage, HomeAbout, HomeGallery, Gallery, HomeFoods

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'text']

class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImage
        fields = ['Image']

class HomeAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAbout
        fields = ['Image']

class HomeGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeGallery
        fields = ['Image', 'AlternateImage']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['Name', 'Image']

class HomeFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFoods
        fields = ['Image']