from django.urls import path
from .views import home, city_weather, register, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('city/', city_weather, name='city_weather'),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', user_profile, name='profile'),
]

