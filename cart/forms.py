from django import forms
from catalog.models import Size
from django.utils.translation import gettext_lazy as _


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_SIZE_CHOICES = Size.objects.all()

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('Количество'))
    size = forms.ModelChoiceField(queryset=PRODUCT_SIZE_CHOICES, label=_('Размер'))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)