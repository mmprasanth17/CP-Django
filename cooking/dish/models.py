from django.db import models
from category.models import Category

# Create your models here.

def dish_image_file_path(instance,dish):
    return '/'.join(['uploads',str(instance.dish),dish])
class Dish(models.Model):
    dish=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to=dish_image_file_path,null=True,blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)