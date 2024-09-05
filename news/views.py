import requests
from datetime import datetime
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.method=="POST":
        data=request.POST
        se=data.get("sear")
        # current_date = datetime.now().date()
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/everything?q={se}&sortBy=popularity&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]
        context={"a":a,"se":se}
    # return render(request,"search.html",context)

    else:

        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]

        context={"a":a}
    return render(request,"index.html",context)

def sports(request):
    if request.method=="POST":
        data=request.POST
        se=data.get("sear")
        # current_date = datetime.now().date()
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/everything?q={se}&sortBy=popularity&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]
        context={"a":a,"se":se}
    else:
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/top-headlines?category=sports&country=us&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]

        context={"a":a}
    return render(request,"sports.html",context)

def business(request):
    if request.method=="POST":
        data=request.POST
        se=data.get("sear")
        # current_date = datetime.now().date()
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/everything?q={se}&sortBy=popularity&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]
        context={"a":a,"se":se}
    else:
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/top-headlines?category=business&country=us&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]

        context={"a":a}
    return render(request,"business.html",context)

def technology(request):
    if request.method=="POST":
        data=request.POST
        se=data.get("sear")
        # current_date = datetime.now().date()
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/everything?q={se}&sortBy=popularity&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]
        context={"a":a,"se":se}
    else:
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/everything?q=technology&apiKey={api_key}')
    
        top_headline=response.json()
        a=top_headline["articles"]

        context={"a":a}
    return render(request,"Technology.html",context)

def entertainment(request):
    if request.method=="POST":
        data=request.POST
        se=data.get("sear")
        # current_date = datetime.now().date()
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/everything?q={se}&sortBy=popularity&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]
        context={"a":a,"se":se}
    else:
        api_key="038c3ac3c0f64423be079a771e96ee2d"
        response=requests.get(f'https://newsapi.org/v2/top-headlines?category=entertainment&country=us&apiKey={api_key}')
        top_headline=response.json()
        a=top_headline["articles"]

        context={"a":a}
    return render(request,"entertainment.html",context)

