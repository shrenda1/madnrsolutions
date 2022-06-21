from email import message
import email
from urllib import request
from django.db import models

# Create your models here.
class vacany(models.Model):
    job_title = models.CharField(max_length=100)
    job_img = models.ImageField(upload_to = 'pics')
    salary = models.IntegerField()
    job_type = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    job_level = models.CharField(max_length=100)
    vacany_number = models.IntegerField()
    educationlevel = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

class carasoul(models.Model):
    img = models.ImageField(upload_to = 'pics')

class sotrecarasoul(models.Model):
    img = models.ImageField(upload_to = 'pics')

class application_form(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

class contactus(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

class laptopinfo(models.Model):
    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    processor = models.CharField(max_length=100)
    graphics = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)

class laptopbrandname(models.Model):
    name = models.CharField(max_length=100)


    