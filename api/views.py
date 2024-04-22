from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, HomeImage, HomeAbout, HomeGallery, Gallery, HomeFoods
from .serializers import ContactSerializer , HomeImageSerializer, HomeAboutSerializer, HomeGallerySerializer, GallerySerializer, HomeFoodsSerializer
from django.shortcuts import render

@api_view(['POST'])
def contact_view(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def HomeAbout_API(request):
    if request.method == 'GET':
        addresses = HomeAbout.objects.all()
        serializer = HomeAboutSerializer(addresses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def gallery_api(request):
    if request.method == 'GET':
        gallery = Gallery.objects.all()
        serializer = GallerySerializer(gallery, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def home_gallery_api(request):
    if request.method == 'GET':
        gallery = HomeGallery.objects.all()
        serializer = HomeGallerySerializer(gallery, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def home_image_api(request):
    if request.method == 'GET':
        images = HomeImage.objects.all()
        serializer = HomeImageSerializer(images, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def home_foods_api(request):
    if request.method == 'GET':
        foods = HomeFoods.objects.all()
        serializer = HomeFoodsSerializer(foods, many=True)
        return Response(serializer.data)


def home_page(request):
    return render(request, 'index.html')
