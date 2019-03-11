from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = ("Categories")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cooperative(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    short_description = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='./pictures/cooperatives/',
                             default='pictures/generic/no_logo.png')
    description = models.CharField(max_length=200)
    phone = PhoneNumberField()
    facebook_profile = models.CharField(max_length=30, default=None)
    address = models.CharField(max_length=50, default=None)
    map_latitude = models.DecimalField(max_digits=9,
                                       decimal_places=7, default=None)
    map_longitude = models.DecimalField(max_digits=9,
                                        decimal_places=7, default=None)
    whatsapp = PhoneNumberField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
