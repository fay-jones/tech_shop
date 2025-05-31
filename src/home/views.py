from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request,'home/home.html')


def products(request):
    Products=Product.objects.all
    context =  {
        'products': Products,
    }
    return render(request,'home/products.html',context)


def contacts(request):
     return render(request,'home/contacts.html')


def about(request):
    members = ['Faith', 'Bruce']
    context = {
        'members': members
    }
    return render(request,'home/about.html', context)
    