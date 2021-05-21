from django.shortcuts import render


def index(request):
    return render(request, 'osaka/index.html', context={'section': 'index'})


def catalog(request):
    return render(request, 'osaka/catalog.html', context={'section': 'catalog'})


def blog(request):
    return render(request, 'osaka/blog.html', context={'section': 'blog'})


def about(request):
    return render(request, 'osaka/about.html', context={'section': 'about'})


def contacts(request):
    return render(request, 'osaka/contacts.html', context={'section': 'contacts'})