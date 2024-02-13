from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    usr=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.first_name

class Newarrival(models.Model):
    newimage=models.ImageField(upload_to='newimage')
    description=models.TextField()
    offer=models.CharField(max_length=100)

    def __str__(self):
        return self.offer
    
class Category(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.cname

class Product(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    price=models.IntegerField()
    image=models.ImageField(null=True)
    cname=models.ForeignKey(Category,on_delete=models.CASCADE)  

    def __str__(self):
        return self.name
          