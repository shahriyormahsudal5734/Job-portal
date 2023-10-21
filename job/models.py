from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Viloyat(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Job(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    pricemin = models.IntegerField()
    pricemax = models.IntegerField()
    manzil = models.CharField(max_length=200)
    phoneNumber =models.CharField(max_length=12)
    category5 = models.ForeignKey(Category,on_delete=models.CASCADE)
    viloyat5 = models.ForeignKey(Viloyat,on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)
    counter = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.title

class Apply_job(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    manzil = models.CharField(max_length=200)
    phoneNumber =models.CharField(max_length=9)
    img = models.ImageField(upload_to='apply/')
    categ = models.ForeignKey(Job,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=20)
    body = models.CharField(max_length=200)
    img = models.ImageField(upload_to='messages/')
    rating = models.IntegerField()
    def __str__(self):
        return self.name

