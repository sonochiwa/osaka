from .models import Contact, Mailing
from .forms import ContactForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required

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

        send_mail(
            'Вы подписались на рассылку.',
            'Мы будем информировать Вас о важных событиях и скидках нашего магазина. Промокод нового пользователя - OSAKASALE',
            'oskastore4you@gmail.com',
            [cd['email']],
            fail_silently=False,
        )

    return HttpResponseRedirect("/")

@staff_member_required
def mailing(request, id):
    contacts = Contact.objects.all()
    for contact in contacts:
        mailing = Mailing.objects.get(id=id)
        subject = mailing.title
        message = mailing.text
        send_mail(subject, message, 
            'oskastore4you@gmail.com', [contact.email])
    return HttpResponseRedirect("/admin/contact/mailing/")
