from django.contrib.admin import AdminSite
from django.contrib.admin.widgets import AdminSplitDateTime
from app_eszam.models import Funkcio, Adalek
from django.contrib import admin

# Register your models here.

admin.site.register(Funkcio)
admin.site.register(Adalek)