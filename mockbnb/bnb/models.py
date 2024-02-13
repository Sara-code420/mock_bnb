from django.db import models

# Create your models here.

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        # Add more property types as needed
    ]

    name = models.CharField(max_length=250)
    type = models.CharField(max_length=100, choices=PROPERTY_TYPES, default='house')
    location = models.CharField(max_length=250, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    coverImage = models.TextField()
    secondaryImage = models.TextField(default='')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    numGuests = models.PositiveIntegerField()
    numBedrooms = models.PositiveIntegerField(default='0')
    numBathrooms = models.PositiveIntegerField(default='0')
