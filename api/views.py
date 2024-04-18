from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, Address, Mailid, mobile, Footer, Services, whatwedos, Menu, MenuItems, Gallery, About, AboutImage, Testimonials, Home, carousel, Homevideo, Homeservices, Homemenus, Homemenuimages,Homegallery, HomeImage, OurTeam
from .serializers import ContactSerializer , AddressSerializer, MailidSerializer, MobileSerializer, FooterSerializer, ServicesSerializer, WhatWeDoSerializer, MenuSerializer, MenuItemsSerializer, GallerySerializer, AboutSerializer, AboutImageSerializer, TestimonialsSerializer, HomeSerializer, CarouselSerializer, HomevideoSerializer, HomeservicesSerializer, HomemenusSerializer, HomemenuimagesSerializer, HomegallerySerializer, HomeImageSerializer, OurTeamSerializer

@api_view(['POST'])
def contact_view(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def address_api(request):
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

# Mailid API view
@api_view(['GET'])
def mailid_api(request):
    if request.method == 'GET':
        mailids = Mailid.objects.all()
        serializer = MailidSerializer(mailids, many=True)
        return Response(serializer.data)

# Mobile API view
@api_view(['GET'])
def mobile_api(request):
    if request.method == 'GET':
        mobiles = mobile.objects.all()
        serializer = MobileSerializer(mobiles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def footer_api(request):
    if request.method == 'GET':
        footers = Footer.objects.all()
        serializer = FooterSerializer(footers, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def services_api(request):
    if request.method == 'GET':
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def whatwedos_api(request):
    if request.method == 'GET':
        Whatwedos = whatwedos.objects.all()
        serializer = WhatWeDoSerializer(Whatwedos, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def menu_api(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def menuitems_api(request):
    if request.method == 'GET':
        menuitems = MenuItems.objects.all()
        serializer = MenuItemsSerializer(menuitems, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def gallery_api(request):
    if request.method == 'GET':
        gallerys = Gallery.objects.all()
        serializer = GallerySerializer(gallerys, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def about_api(request):
    if request.method == 'GET':
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def testimonials_api(request):
    if request.method == 'GET':
        testimonials = Testimonials.objects.all()
        serializer = TestimonialsSerializer(testimonials, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def home_api(request):
    if request.method == 'GET':
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def carousel_api(request):
    if request.method == 'GET':
        carousels = carousel.objects.all()
        serializer = CarouselSerializer(carousels, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def homevideo_api(request):
    if request.method == 'GET':
        homevideos = Homevideo.objects.all()
        serializer = HomevideoSerializer(homevideos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def homeservices_api(request):
    if request.method == 'GET':
        homeservices = Homeservices.objects.all()
        serializer = HomeservicesSerializer(homeservices, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def homemenu_api(request):
    if request.method == 'GET':
        homemenu = Homemenus.objects.all()
        serializer = HomemenusSerializer(homemenu, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def homemenuimages_api(request):
    if request.method == 'GET':
        homemenuimages = Homemenuimages.objects.all()
        serializer = HomemenuimagesSerializer(homemenuimages, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def homegallery_api(request):
    if request.method == 'GET':
        homegallery = Homegallery.objects.all()
        serializer = HomegallerySerializer(homegallery, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def homeimage_api(request):
    if request.method == 'GET':
        homeimage = HomeImage.objects.all()
        serializer = HomeImageSerializer(homeimage, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ourteam_api(request):
    if request.method == 'GET':
        ourteam = OurTeam.objects.all()
        serializer = OurTeamSerializer(ourteam, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def Aboutimage_api(request):
    if request.method == 'GET':
        aboutimage = AboutImage.objects.all()
        serializer = AboutImageSerializer(aboutimage, many=True)
        return Response(serializer.data)