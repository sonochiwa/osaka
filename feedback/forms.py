from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['email', 'text']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent'}),
            'text': forms.TextInput(attrs={'class': 'editContent'})
        }