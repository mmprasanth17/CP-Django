from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author_id=serializers.IntegerField(write_only = True)
    class Meta:
        model=Book
        fields=['id','title','rating','author_id']
        read_only_fields=['id']
        
