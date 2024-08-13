from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Q
# Create your models here.


class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(35)])#Validator
    city=models.CharField(max_length=100,null=True)
    rating=models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)],null=True)
    
    
    def __str__(self) -> str:
        return (f'Full Name : {self.first_name} {self.last_name} Age :{self.age} City : {self.city}')
    