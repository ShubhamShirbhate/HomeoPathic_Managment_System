from django.db import models
from django.contrib.auth.models import User

class Patient_info(models.Model):
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Treatment(models.Model):
    add_treat = models.TextField(blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

class History(models.Model):
    add_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)