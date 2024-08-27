from django.urls import path
from . import views
from .views import AddFormView, PostDetailView

urlpatterns = [
    path('', views.index, name='index'),  # Ensure you provide a name for the index path
    path('form/<int:post_id>/', AddFormView.as_view(), name='add_form'),  # Using CBV for the form
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),  # Using CBV for post detail
    path('posts/', views.PostListView.as_view(), name='post_list'),  # Assuming you're using a ListView for posts
]
