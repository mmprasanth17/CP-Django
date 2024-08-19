from django.urls import path
from .import views
urlpatterns = [
    # path('form/', views.index, name='form'),
    path('index/',views.feedbackform,name='feedbackform'),
    path('thankyou/',views.thanku,name = 'thankyou'),
]