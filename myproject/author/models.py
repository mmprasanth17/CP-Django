from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Q
from django.utils.text import slugify
# Create your models here.


class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(2)])#Validator
    city=models.CharField(max_length=100,null=True)
    rating=models.FloatField(validators=[MaxValueValidator(5),MinValueValidator(1)],null=True)
    full_name=models.CharField(max_length=20,null=True)
    #jk Rowling ===> jk-rowling
    
    slug=models.SlugField(default='',db_index=True,editable=False)    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.full_name)
        super().save(*args,**kwargs)
        
    
    def __str__(self) -> str:
        return (f'Full Name : {self.first_name} {self.last_name} Age :{self.age} City : {self.city}')
    