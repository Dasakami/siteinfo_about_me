"""
URL configuration for dan_dasakami project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path  # Добавляем re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.conf.urls import handler404, handler500,handler403

handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'
handler403 = 'main.views.permission_denied'

urlpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # Заменили url на re_path
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
