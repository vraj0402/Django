from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    a_info = models.CharField(max_length=30)
    date=models.DateField()

