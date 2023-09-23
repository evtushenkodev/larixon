from django.contrib import admin

from .models import Category, City, Advert


class AdvertAdmin(admin.ModelAdmin):
    readonly_fields = ('views',)


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Category)
admin.site.register(City)

