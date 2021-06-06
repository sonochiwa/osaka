from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    def __init__(self, sizes=[], *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['size'] = forms.ChoiceField(choices=tuple([(str(name), str(name)) for name in sizes]))

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(required=False, initial=False,
        widget=forms.HiddenInput)