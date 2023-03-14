from django.urls import path, include
from .views import RegisterView, user_profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', RegisterView.as_view(), name='register'),
    path('profile/', user_profile, name='user_profile'),
]




# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register', views.register_request, name='register'),
#     path('login', views.login_request, name='login'),
#     path('logout', views.logout_request, name='logout'),
# ]
