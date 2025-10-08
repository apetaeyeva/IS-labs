import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    city = request.GET.get('city')

    if city:
        API_KEY = "7fd4cd22ccc1d7f2a2e08f31e1deb6ae"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data = {'error': 'Город не найден'}

    return render(request, 'weather/index.html', {'weather': weather_data})