import math
from django.shortcuts import render, redirect
from .forms import LocationForm, ShopRegistrationForm
from math import radians, cos, sin, sqrt, atan2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Shop
from .serializers import ShopSerializer
from django.contrib.auth import login

def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST)
        redirect_to_search=request.POST.get('redirect_to_success') == 'on'
        if form.is_valid():
            user=form.save()  

            if redirect_to_search:
                return redirect('search_shop')
            return render(request,'shop/registration_success.html')
    else:
        form = ShopRegistrationForm()
    
    return render(request, 'Shop/register_shop.html', {'form': form})




def haversine(lat1, lon1, lat2, lon2):
  
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    R = 6371  
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c



def shop_search(request):
    shops = []  
    form = LocationForm()  

    if request.method == 'GET':
        form = LocationForm(request.GET) 
        if form.is_valid():  
            user_lat = form.cleaned_data['latitude']  
            user_lon = form.cleaned_data['longitude']  

            
            for shop in Shop.objects.all():
                distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude) 
                shops.append((shop, distance)) 
            
            shops.sort(key=lambda x: x[1]) 

    return render(request, 'shop/search_shops.html', {'form': form, 'shops': shops})  