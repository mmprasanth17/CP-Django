from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index),
    path('<str:author>', views.author_details, name='author-details'),
]