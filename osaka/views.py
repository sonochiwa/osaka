from django.shortcuts import render
from catalog.models import Product


def index(request):
    discount_products = Product.objects.filter(discount__gt=0)[:4]
    return render(request, 'osaka/index.html', context={'section': 'index', 'products': discount_products})
    

def about(request):
    return render(request, 'osaka/about.html', context={'section': 'about'})

def contacts(request):
    return render(request, 'osaka/contacts.html', context={'section': 'contacts'})