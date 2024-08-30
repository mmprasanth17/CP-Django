from django.shortcuts import render
from . models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
 
# Create your views here.
class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        return self.serializer_class
 
#get all authors
    def list(self,request):
        try:
            author_objs = Book.objects.all()
            serializer = self.get_serializer(author_objs,many=True)
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
