from django.urls import path,include
from .import views

urlpatterns = [
    # path('index', views.index),
    # path('name',views.name),
    
    # path('<month>', views.monthly_details),
    
    path('<int:month>', views.monthly_details_by_number),  #1
    path('<str:month>', views.monthly_details, name='month-details')
]
# <palceholder>
# month/1 ---> month/january    
# month/2 ---> month/february