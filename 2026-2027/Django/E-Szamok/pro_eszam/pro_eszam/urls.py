"""
URL configuration for pro_eszam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app_eszam.views import view_2kerulendo, view_import, view_import_kuld, view_index, view_3karamell
from encodings import latin_1
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', view_import),
    path('import/kuld/', view_import_kuld),
    path('', view_index),
    path('2kerulendo/', view_2kerulendo),
    path('3karamell/', view_3karamell),
]
