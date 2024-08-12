from django.db import models

# Create your models here.
class dishmodel(models.Model):
    dish_name=models.CharField(max_length=50)
    dish_price=models.CharField(max_length=50)