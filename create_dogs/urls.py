from django.urls import path

from . import views

urlpatterns = [
    path('', views.dog_heaven, name='dog_heaven'),
    path('create/', views.CreatePetPage.as_view(), name='create_dog'),
    path('edit/<int:pk>/', views.PetEditPage.as_view(), name='edit_pet'),
    path('delete/<int:pk>/', views.PetDelete.as_view(), name='delete_dog'),
    path('view/<int:pk>/', views.DogPage.as_view(), name='dog_detail')
]