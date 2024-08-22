from django.urls import path
from .import views 

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('card/<int:post_id>/', views.card_details, name='card_details'),
    path('add/', views.add_product, name='add_product'),
    path('allpost/', views.all_post, name='all_post'),
    
]