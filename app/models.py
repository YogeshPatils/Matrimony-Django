from django.db import models

# Create your models here.
class MatrimonyModel(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    religion=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    salary=models.IntegerField()
    phone=models.IntegerField()