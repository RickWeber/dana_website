from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    short_name = models.CharField(max_length=25)
    description = RichTextField()

class Resource(models.Model):
    short_name = models.CharField(max_length=25)
    description = RichTextField()
    url = models.URLField()

class PaymentOption(models.Model):
    """A class to hold information on insurance providers, cash prices, etc."""
    pass

class Counselor(models.Model):
    """A class to hold data and methods about Dana"""
    first_name = models.CharField(default="Dana", max_length=35)
    last_name = models.CharField(default="Ellis", max_length=35)
    phone_number = models.CharField(default="631-255-5020", max_length=15)
    email = models.EmailField()
    def __str__(self):
        return f"{first_name} {last_name}"
