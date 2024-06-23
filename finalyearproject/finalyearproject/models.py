# <<<<<<< HEAD
import os
from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

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
        is_new_instance = not self.pk  # Check if it's a new instance (not saved to the database yet)
        
        if is_new_instance and self.profile_picture:
            extension = self.profile_picture.name.split('.')[-1]
            new_name = f'{self.employee_id}.{extension}'
            self.profile_picture.name = new_name

        super().save(*args, **kwargs)
class Admin(models.Model):
    name = models.CharField(max_length=255)
    admin_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='img/', blank=True, null=True)
    def save(self, *args, **kwargs):
        is_new_instance = not self.pk  # Check if it's a new instance (not saved to the database yet)
        
        if is_new_instance and self.profile_picture:
            extension = self.profile_picture.name.split('.')[-1]
            new_name = f'{self.admin_id}.{extension}'
            self.profile_picture.name = new_name
        super().save(*args, **kwargs)
class Attendance(models.Model):
    person_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.person_id} - {self.date} - {self.time}"
def __str__(self):
     return self.title 
class Guard(models.Model):
    name = models.CharField(max_length=255)
    guard_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='img/', null=True, blank=True)
    def save(self, *args, **kwargs):
        is_new_instance = not self.pk  # Check if it's a new instance (not saved to the database yet)
        
        if is_new_instance and self.profile_picture:
            extension = self.profile_picture.name.split('.')[-1]
            new_name = f'{self.guard_id}.{extension}'
            self.profile_picture.name = new_name

        super().save(*args, **kwargs)
class TemporaryPerson(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.CharField(max_length=10)
    reason_for_visiting = models.TextField()
    expiration_datetime = models.DateTimeField()
    photo = models.ImageField(upload_to='img/',null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.photo:
            extension = self.photo.name.split('.')[-1]
            new_name = f'{self.person_id}.{extension}'
            self.photo.name = new_name
        super().save(*args, **kwargs)
