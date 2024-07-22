"""webdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


=======


from main.views import home

>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038


urlpatterns = [
    path('', include('main.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
<<<<<<< HEAD
    path("admin/", admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
=======
    path('conversation/', include('conversation.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038
