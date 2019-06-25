from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostCreateView.as_view(), name='create_dog_post'),
    path('edit/', views.dog_post_edit_page, name='edit_dog_post'),
    path('delete/', views.deleate_dog_post, name='delete_dog_post'),
    path('view/<int:pk>/', views.DogPostDetailView.as_view(), name='dog_post_detail'),
    path('social/', views.pet_social, name='pet_social'),
]