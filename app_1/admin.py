from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ContentManager)
class Custom_admin(admin.ModelAdmin):
    list_display = ['title','image_tag',]