# <<<<<<< HEAD
import os
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
    profile_picture = models.ImageField(upload_to='img/', null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.profile_picture:
            extension = os.path.splitext(self.profile_picture.name)[1]
            new_name = f'{self.employee_id}.{extension}'
            self.profile_picture.name = new_name
        super().save(*args, **kwargs)
def __str__(self):
     return self.title