from django.db import models

# Create your models here.

class User(models.Model):
    login_name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    status = models.IntegerField(max_length=11)
    create_date = models.DateField
    user_name = models.CharField(max_length=20)
    face_url = models.CharField(max_length=255)
    face_path = models.CharField(max_length=255)
