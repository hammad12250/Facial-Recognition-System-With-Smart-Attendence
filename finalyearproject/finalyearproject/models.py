# <<<<<<< HEAD
from django.db import models

class Camera(models.Model):
    camera_link = models.CharField(max_length=255)


# =======
from django.db import models
class RtspCamera(models.Model):
    camera_link = models.CharField(max_length=255)
# >>>>>>> 17061208419e3c5f98276d9d37d7c4fceac65be7
