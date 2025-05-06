from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from cloudinary_storage.storage import MediaCloudinaryStorage

class Article(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, unique=True)
    content = CKEditor5Field(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='help_article_images/', blank=True, null=True, storage=MediaCloudinaryStorage())

    def __str__(self):
        return self.title
# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Отзыв от {self.name}'
