from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    return render(request,'shop/index.html',{'Products':all_products})

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at seacrh")

def productView(request):
    return HttpResponse("We are at productview")

def checkout(request):
    return HttpResponse("We are at checkout")