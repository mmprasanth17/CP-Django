from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Review(models.Model):
    user_name=models.CharField(max_length=20)
    text=models.CharField(max_length=100)
    rating=models.FloatField(validators=[MaxValueValidator(5),MinValueValidator(1)])    
    
    