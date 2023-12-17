# <<<<<<< HEAD
from django.db import models

class Camera(models.Model):
    camera_link = models.CharField(max_length=255)
class RtspCamera(models.Model):
    camera_link = models.CharField(max_length=255)
class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
def __str__(self):
     return self.title