from django.urls import path
from .import views 

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('card/<slug:post_id>/', views.card_details, name='card_details'),
    path('add/', views.add_bike, name='add_bike'),
    path('allpost/', views.all_post, name='all_post'), 
    path('command/', views.commentCreateView.as_view(), name='command'), 
]