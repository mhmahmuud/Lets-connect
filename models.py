from django.db import models

# Create your models here.

class Add_User(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50, null=True)
    state_of_origin=models.CharField(max_length=50, null=True)
    lga=models.CharField(max_length=50, null=True)
    country_of_residence=models.CharField(max_length=50, null=True)
    state_of_residence=models.CharField(max_length=50, null=True)
    city=models.CharField(max_length=50, null=True)
    occupation=models.CharField(max_length=50, null=True)
    place_of_work=models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.username
    