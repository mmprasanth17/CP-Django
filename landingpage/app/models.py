from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Q
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class user(models.Model):
    # image=models.URLField(max_length=1000,null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    product_name=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=400,null=True)
    cost=models.IntegerField(null=True)
    rating=models.FloatField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    date = models.DateField(default=timezone.now,null=True)  
    time = models.TimeField(default=timezone.now,null=True)
    current_time = models.DateTimeField(default=timezone.now,null=True)
    
    def save(self,*args,**kwargs):
        # self.slug=slugify(self.product_name)
        super().save(*args,**kwargs)
        
    
    def __str__(self) -> str:
        return (f'Prodact : {self.product_name}')
    