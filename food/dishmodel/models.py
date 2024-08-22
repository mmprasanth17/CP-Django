from django.db import models

# Create your models here.

class Address(models.Model):
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    street_no=models.IntegerField()
    
class Chief(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.ForeignKey(Address,on_delete=models.CASCADE,null=True)
    
class dishmodel(models.Model):
    dish_name=models.CharField(max_length=50)
    dish_price=models.CharField(max_length=50)
    chief=models.ForeignKey(Chief,on_delete=models.CASCADE,null=True)