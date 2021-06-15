from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['email', 'text']
        labels = {
            'email': '',
            'text': ''
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'E-mail'}),
            'text': forms.Textarea(attrs={'class': 'editContent', 'placeholder': 'Текст'})
        }