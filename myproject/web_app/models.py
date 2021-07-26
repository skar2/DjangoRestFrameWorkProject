from django.db import models
from datetime import datetime,date

# Create your models here.
class BasicDetails(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    fathername = models.CharField(max_length=10)
    mothername = models.CharField(max_length=10)
    dob=models.DateField(max_length=8)
    gender=models.CharField(max_length=6)
    about=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)

    def str(self):
        return self.firstname


class Education(models.Model):
    course_name=models.CharField(max_length=10)
    University=models.CharField(max_length=10)
    passing_year=models.IntegerField(max_length=4)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)

    def str(self):
        return self.course_name