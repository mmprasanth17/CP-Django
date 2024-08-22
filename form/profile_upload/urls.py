from django.urls import path
from .import views

urlpatterns = [
    # path('',views.home),
    path('',views.CreateProfileView.as_view()),
    path('ren',views.Profileview.as_view())
    # path('',views.CreateProfileView.as_view()),
]