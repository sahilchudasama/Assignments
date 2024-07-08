from django import forms
from .models import FormData

class ContactForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'email', 'message']
