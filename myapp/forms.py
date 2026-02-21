from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, EmailInput
from .models import Form

class Contactform(forms.ModelForm):
    class Meta:
        model  = Form
        fields = ['name','last_name','number','email','type','text']
        widgets = {
            'name':TextInput(attrs={
                'placeholder':"Your name",
                'class': "input"
            }),
            'last_name':TextInput(attrs={
                'placeholder':"Your last name",
                'class': "input"
            }),
            'number':TextInput(attrs={
                'placeholder':"Your phone number",
                'class': "input"
            }),
            'email':EmailInput(attrs={
                'placeholder':"Your email",
                'class': "input"
            }),
            'type':Select(attrs={
                'class': "input"
            }),
            'text':Textarea(attrs={
                'class': "input_area"
            }),

        }