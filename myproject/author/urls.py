from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>/', views.author_info, name='author_info'),
    path('<slug:slug>/', views.author_slug, name='author-slug'),

   
   path('<str:author>', views.author_details, name='author-details'),
    
]