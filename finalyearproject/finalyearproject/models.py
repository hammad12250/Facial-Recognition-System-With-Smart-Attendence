from django.db import models

class Camera(models.Model):
    camera_link = models.CharField(max_length=255)


