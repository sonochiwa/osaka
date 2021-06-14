from django.shortcuts import render

def contacts(request, category_slug=None):
    category = None


    return render(request, 'feedback/contacts.html',
                {'contacts': contacts})