from django.contrib import admin
from .models import *

@admin.register(product)
class product_admin(admin.ModelAdmin):
    list_display=('name','price','description','image',)
@admin.register(reachus)
class reachus_admin(admin.ModelAdmin):
    list_display=('name','email','PhoneNumber','description',)
