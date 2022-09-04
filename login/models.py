from statistics import mode
from django.db import models

# Create your models here.
class UserDetail(models.Model):
    User_name = models.CharField(max_length=200)
    #User_birthday = models.DateTimeField()
    # User_height = models.IntegerField()
    # User_pic = models.ImageField()

class FileModel(models.Model):
    doc = models.FileField(upload_to='media/')