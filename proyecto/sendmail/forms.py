# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,label='Correo')
    subject = forms.CharField(required=True,label='Asunto')
    message = forms.CharField(widget=forms.Textarea, required=True,label='Mensaje')