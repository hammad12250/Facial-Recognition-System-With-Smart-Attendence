from django.db import models
class RtspCamera(models.Model):
    camera_link = models.CharField(max_length=255)