from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('about', views.PetcoCreateView.as_view(), name='about'),
    path('update', views.PetcoUpdateView.as_view(), name='update'),
    path('logout', views.logout, name="logout")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIAFILES_LOCATION, document_root=settings.DEFAULT_FILE_STORAGE)