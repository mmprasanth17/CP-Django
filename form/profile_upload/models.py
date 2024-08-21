from django.db import models

class Profileimage(models.Model):
    userimage = models.FileField(upload_to='images')
