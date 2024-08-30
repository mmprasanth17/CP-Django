from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    categoryName=serializers.CharField(write_only = True)
    class Meta:
        model=Category
        fields=['id','categoryName']
        read_only_fields=['id']
        
