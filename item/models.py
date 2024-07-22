from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=255)

<<<<<<< HEAD
=======

>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038
    def __str__(self):
        return self.city


<<<<<<< HEAD


class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, max_length=255, on_delete=models.CASCADE)
=======
class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(City, max_length=255)

>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038

    def __str__(self):
        return self.address
    


<<<<<<< HEAD


=======
>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038
class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = "Categories"
<<<<<<< HEAD
=======

>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038
    
    def __str__(self):
        return self.name
    
    


class Item(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200, unique=True)
    destinations = models.CharField(blank=True, null=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    images = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    published_by = models.ForeignKey(User, related_name='items_author', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(blank=True, null=True, max_length=150)
    max_persons = models.CharField(blank=True, null=True, max_length=50)
    pool = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    bedrooms = models.PositiveSmallIntegerField(blank=True, null=True)
    bathrooms = models.PositiveSmallIntegerField(blank=True, null=True)
    persons = models.PositiveSmallIntegerField(blank=True, null=True)
    places = models.BooleanField(default=False)
    restaurants = models.BooleanField(default=False)
    vacations = models.BooleanField(default=False)
    activities = models.BooleanField(default=False)
    trip = models.BooleanField(default=False)
<<<<<<< HEAD
    start_date = models.DateField(default=False)
    end_date = models.DateField(default=False)
=======


>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038


    def __str__(self):
        return self.name
