from django.contrib import admin
from .models import Contact, HomeAbout, HomeGallery, Gallery, HomeImage, HomeFoods

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'text')
    search_fields = ('name', 'phone', 'email', 'text') 

admin.site.register(Contact, ContactAdmin)
admin.site.register(HomeAbout)
admin.site.register(HomeGallery)
admin.site.register(Gallery)
admin.site.register(HomeImage)
admin.site.register(HomeFoods)