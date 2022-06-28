from email import message
from django.db import models

# Create your models here.
class Signup(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)


class qur(models.Model):
   # uid = models.CharField(max_length=40,default=0)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100) 
    subject = models.CharField(max_length=40,default=0)   
    message = models.CharField(max_length=40,default=0)

class multi_file(models.Model):
	userid=models.CharField(max_length=40)
	file1 = models.FileField(null=True,blank=True)
	file2 = models.FileField(null=True,blank=True)
	file3 = models.FileField(null=True,blank=True)
	file4 = models.FileField(null=True,blank=True)
	def __str__(self):
		return self.file1   


class img_table(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    img = models.FileField()


class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    phone=models.IntegerField(max_length=30)