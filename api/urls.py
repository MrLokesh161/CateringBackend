from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view, address_api, mailid_api, mobile_api, footer_api, services_api, whatwedos_api, menu_api, menuitems_api, gallery_api, about_api, testimonials_api, home_api, carousel_api, homevideo_api, homeservices_api, homemenu_api, homemenuimages_api, homegallery_api, homeimage_api, ourteam_api, Aboutimage_api

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('address/', address_api, name='address_api'),
    path('mailid/', mailid_api, name='mailid_api'),
    path('mobile/', mobile_api, name='mobile_api'),
    path('footer/', footer_api, name='footer_api'),
    path('services/', services_api, name='services_api'),
    path('whatwedos/', whatwedos_api, name='whatwedos_api'),
    path('menu/', menu_api, name='menu_api'),
    path('menuitems/', menuitems_api, name='menuitems_api'),
    path('gallery/', gallery_api, name='gallery_api'),
    path('about/', about_api, name='about_api'),
    path('testimonials/', testimonials_api, name='testimonials_api'),
    path('home/', home_api, name='home_api'),
    path('carousel/', carousel_api, name='carousel_api'),
    path('homevideo/', homevideo_api, name='homevideo_api'),
    path('homeservices/', homeservices_api, name='homeservices_api'),
    path('homemenu/', homemenu_api, name='homemenu_api'),
    path('homemenuimages/', homemenuimages_api, name='homemenuimages_api'),
    path('homegallery/', homegallery_api, name='homegallery_api'),
    path('homeimage/', homeimage_api, name='homeimage_api'),
    path('ourteam/', ourteam_api, name='ourteam_api'),
    path('aboutimage/', Aboutimage_api, name='Aboutimage_api'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)