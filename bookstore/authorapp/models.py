from django.db import models

# Create your models here.

def author_image_file_path(instance,filename):
    return '/'.join(['uploads',str(instance.name),filename])

class Author(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()   
    city=models.CharField(max_length=100)
    image=models.ImageField(upload_to=author_image_file_path,null=True,blank=True)