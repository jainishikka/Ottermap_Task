from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=('name','owner','latitude','longitude')

# Register your models here.
