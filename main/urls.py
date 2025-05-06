from django.urls import include,path
from django.template import Template
from django.views.generic import TemplateView
from .views import custom_upload_function, articles, article_detail, main,contacts
urlpatterns  = [
    path('', main, name='home'),
    path('articles/', articles, name='articles'),
    path('article/<slug:slug>', article_detail, name='article_detail'),
    path('contacts/', contacts, name='contacts'),
    path('about/', TemplateView.as_view(template_name='main/about.html'), name='about'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('projects/', TemplateView.as_view(template_name='main/projects.html'), name='projects'),
    path('ckeditor/upload/', custom_upload_function , name='ckeditor_upload'),
]