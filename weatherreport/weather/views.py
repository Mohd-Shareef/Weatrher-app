from django.shortcuts import render,redirect
from django.contrib import messages
import json
import urllib.request

def index(request):
    try:
        if request.method=="POST":
            city = request.POST.get('city')
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=54b67752468f5a97d6949670a342df43').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon'])+ ' '+
                str(json_data['coord']['lat']),
                "temp":str(int(json_data['main']['temp']-273))+' °C',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
                "main":str(json_data['weather'][0]['main']),
                'icon': json_data['weather'][0]['icon'],
                "description":str(json_data['weather'][0]['description']),
                "city":city
        }
        else:
             city=''
             data={}
    except:
            data={}
    return render(request,"index.html",{'city':city,'data':data})
