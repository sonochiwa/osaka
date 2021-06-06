from .models import Contact
from .forms import ContactForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

@require_POST
def subscription(request):
    cantact_form = ContactForm(request.POST)
    if cantact_form.is_valid():
        cd = cantact_form.cleaned_data
        email = cd["email"]
        try:
            contact = Contact.objects.get(email=email)
        except ObjectDoesNotExist:
            cantact_form.save()
    return HttpResponseRedirect("/")