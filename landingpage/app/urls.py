from django.urls import path
from .import views 

urlpatterns = [
    path('land/', views.landing_page, name='landing'),
    path('card/<int:post_id>/', views.card_details, name='card_details'),
    path('add/', views.add_bike, name='add_bike'),
    path('allpost/', views.all_post, name='all_post'),  
]