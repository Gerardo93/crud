# -*- encoding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrarForm(ModelForm):
    password2= forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2' ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de Usuario',
            'email': 'Correo',
            'password': 'Contraseña',

        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'col-md-4 form-control'}),
            'username': forms.TextInput(attrs={'class': 'col-md-4 form-control'}),
            'email': forms.TextInput(attrs={'class': 'col-md-4 form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'col-md-4 form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'col-md-4 form-control'}),

        }
    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2