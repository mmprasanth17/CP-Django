from django.urls import path
from .import views
urlpatterns = [
    # path('form/', views.index, name='form'),
    # path('index/',views.feedbackform,name='feedbackform'),
    path('form/', views.feedbackform.as_view(), name='feedbackform'),
    path('thankyou/',views.ThankyouView.as_view(),name = 'thankyou'),
    path('list/',views.feedbacklistView.as_view(),name = 'list'),
   
    

]