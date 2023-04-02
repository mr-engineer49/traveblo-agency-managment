from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = "Categories"

    
    def __str__(self):
        return self.name
    


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    images = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    published_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
