from django.contrib import admin
from .models import Contact, Address, Mailid, mobile, Footer, Services, whatwedos, Menu, MenuItems, Gallery, About, AboutImage, Testimonials, Home, carousel, Homevideo, Homeservices, Homemenus, Homemenuimages, Homegallery, HomeImage, OurTeam


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'text')
    search_fields = ('name', 'phone', 'email', 'text') 

admin.site.register(Contact, ContactAdmin)
admin.site.register(Address)
admin.site.register(Mailid)
admin.site.register(mobile)

admin.site.register(Footer)
admin.site.register(Services)
admin.site.register(whatwedos)
admin.site.register(Menu)
admin.site.register(MenuItems)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(AboutImage)
admin.site.register(Testimonials)
admin.site.register(Home)
admin.site.register(carousel)
admin.site.register(Homevideo)
admin.site.register(Homeservices)
admin.site.register(Homemenus)
admin.site.register(Homemenuimages)
admin.site.register(Homegallery)
admin.site.register(HomeImage)
admin.site.register(OurTeam)
