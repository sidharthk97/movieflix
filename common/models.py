from django.db import models



# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=40, default="firstname")
    last_name = models.CharField(max_length=40, default="lastname")
    email = models.CharField(max_length=100, default="email")
    mobile = models.CharField(max_length=40, default="0000")
    password = models.CharField(max_length=40, default="password")

    
