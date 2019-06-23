from django.urls import path, reverse
from . import views
from .models import CreatePet
urlpatterns = [
    path('', views.dog_heaven, name='dog_heaven'),
    path('create/', views.CreateDogPage.as_view(), name='create_dog'),
    path('edit/', views.dog_edit_page, name='edit_dog'),
    path('delete/', views.deleate_dog, name='delete_dog'),
    path('view/', views.dog_detail, name='dog_detail')
]