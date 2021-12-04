from django import forms
from django.db.models import fields
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta: 
        model = Persona
        fields = '__all__'
        widgets = {
        'contrasenia': forms.PasswordInput(),
    }