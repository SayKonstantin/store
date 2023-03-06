from django.urls import path, include
from .views import RegisterView, ProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', RegisterView.as_view(), name='register'),
    path('<int:pk>', ProfileView.as_view(), name='profile'),


]
