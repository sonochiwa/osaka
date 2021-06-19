from django import forms
from .models import Order, Mart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    def __init__(self, sizes=[], *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['size'] = forms.ChoiceField(choices=tuple([(str(name), str(name)) for name in sizes]))

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(required=False, initial=False,
        widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['mart'] = forms.ModelChoiceField(queryset=Mart.objects.all(), empty_label='Выберете...', required=False)

    class Meta:
        model = Order
        fields = ['mart', 'address', 'index', 'promo']
        labels = {
            'mart': '',
            'address': '',
            'index': '',
            'promo': '',
        }
        widgets = {
            'mart': forms.TextInput(attrs={'class': 'editContent', 'option': 'Магазин'}),
            'address': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Домашний адрес'}),
            'index': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Почтовый индекс'}),
            'promo': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Введите промо-код'})
        }
