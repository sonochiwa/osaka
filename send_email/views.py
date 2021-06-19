from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .service import send

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'send_email/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form) 