from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewset
 
router = DefaultRouter()
router.register('', AuthorViewset, basename='authorapp')
app_name ='authorapp'
 
urlpatterns=[
    path('', include(router.urls))
]