from django.urls import path
from . import views

urlpatterns = [
    path('', views.dog_post_page, name='create_dog_post'),
    path('edit/', views.dog_post_edit_page, name='edit_dog_post'),
    path('delete/', views.deleate_dog_post, name='delete_dog_post'),
    path('view/', views.dog_post_detail, name='dog_post_detail')
]