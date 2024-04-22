from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view, HomeAbout_API, gallery_api, home_gallery_api, home_image_api, home_foods_api, home_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('contact/', contact_view, name='contact'),
    path('homeabout/', HomeAbout_API, name='homeabout'),
    path('gallery/', gallery_api, name='gallery'),
    path('homegallery/', home_gallery_api, name='homegallery'),
    path('homeimage/', home_image_api, name='homeimage'),
    path('homefoods/', home_foods_api, name='homefoods'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)