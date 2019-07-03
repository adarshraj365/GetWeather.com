from django.shortcuts import render
import requests



# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fd3905e729f0a07eea736dc9ddf545ce'
    

  

    city= 'Mumbai'
   

   

    
    r = requests.get(url.format(city)).json()

    

    city_weather = {

        'city': city  ,
        'temp': r['main']['temp'] ,
        'description': r['weather'][0]['description'] ,
        'icon':   r['weather'][0]['icon']  ,
    }

        


    dict = {'city_weather':city_weather}

  
    return render(request,'html/index.html',dict)


def find_weather(request):

    city = request.GET.get('text','default')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fd3905e729f0a07eea736dc9ddf545ce'
    r = requests.get(url.format(city)).json()

    city_weather = {

            'city': city  ,
            'temp': r['main']['temp'] ,
            'description': r['weather'][0]['description'] ,
            'icon':   r['weather'][0]['icon']  ,
        }
    dict = {'city_weather':city_weather}
    return render(request,'html/index.html',dict)