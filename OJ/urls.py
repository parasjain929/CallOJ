"""OJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from OJ.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('dashboard/',include('problems.urls')),
    path('contest/',include('contest.urls')),
    path('userprofile/',include('userprofile.urls')),
    path('about1/',aboutview1),
    path('about2/',aboutview2),
    path('about3/',aboutview3),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)