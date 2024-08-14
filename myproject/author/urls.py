from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index),
    path('<slug:slug>/', views.author_slug, name='author-slug'),

   path('<int:id>/', views.author_info, name='author-info'),
   path('<str:author>', views.author_details, name='author-details'),
    
]