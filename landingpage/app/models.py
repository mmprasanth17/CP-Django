from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Q
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class user(models.Model):
    # image=models.URLField(max_length=1000,null=True)
    Image = models.FileField(upload_to='images/', null=True, blank=True)

    BikeName=models.CharField(max_length=50,null=True)
    Description=models.CharField(max_length=400,null=True)
    Date = models.DateField(default=timezone.now,null=True)  
    Time = models.TimeField(default=timezone.now,null=True)
    Current_time = models.DateTimeField(default=timezone.now,null=True)
    
    def save(self,*args,**kwargs):
        # self.slug=slugify(self.product_name)
        super().save(*args,**kwargs)
        
    
    def __str__(self) -> str:
        return (f'Prodact : {self.BikeName}')
    