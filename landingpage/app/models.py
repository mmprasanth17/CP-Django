from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Q
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class TagLine(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class user(models.Model):
    # image=models.URLField(max_length=1000,null=True)
    Image = models.FileField(upload_to='images/', null=True, blank=True)

    BikeName=models.CharField(max_length=50,null=True)
    Description=models.CharField(max_length=400,null=True)
    Date = models.DateField(default=timezone.now,null=True)  
    Time = models.TimeField(default=timezone.now,null=True)
    Current_time = models.DateTimeField(default=timezone.now,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagLine,null=True)
    slug=models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.BikeName)
        super().save(*args,**kwargs)
        
    
    def __str__(self) -> str:
        return (f'Bike : {self.BikeName}')
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post}"
    