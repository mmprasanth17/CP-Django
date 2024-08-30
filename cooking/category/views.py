from django.shortcuts import render
from . models import Category
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
 
# Create your views here.
class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        return self.serializer_class
 
#get all authors
    def list(self,request):
        try:
            category_objs = Category.objects.all()
            serializer = self.get_serializer(category_objs,many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data':serializer.data
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })