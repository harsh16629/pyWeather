from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SearchHistory
from django.contrib.auth.decorators import login_required
import requests

def home(request):
    return render(request, 'weather/home.html')

def city_weather(request):
    city = request.GET.get('city')

    if city:
        #api_key = "enter_your_openweathermap_API_KEY_here"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'visibility': data['visibility'] / 1000,  # Convert meters to kilometers
                'min_temp': data['main']['temp_min'],
                'max_temp': data['main']['temp_max'],
                'pressure': data['main']['pressure'],
                'weather_description': data['weather'][0]['description'],
            }
        else:
            weather_data = {
                'error': 'City not found or API error'
            }
    else:
        weather_data = {}

    return render(request, 'weather/city_weather.html', weather_data)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')  
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'weather/register.html')

@login_required
def user_profile(request):
    # Fetch the search history and comments created by the logged-in user
    search_history = SearchHistory.objects.filter(user=request.user).order_by('-search_date')
    return render(request, 'weather/profile.html', {
        'user': request.user,
        'search_history': search_history
    })
