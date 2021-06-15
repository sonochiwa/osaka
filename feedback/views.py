from django.shortcuts import render, redirect
from .forms import FeedbackForm

def contacts(request):
    if request.method == 'POST': 
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('/feedback')
                    
    else:
        form = FeedbackForm()
    return render(request, 'feedback/contacts.html', {'contacts_form': form })