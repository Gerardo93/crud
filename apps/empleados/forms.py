# -*- encoding:UTF-8 -*-
import re
from django import forms
from datetime import date, timedelta

from models import Empleado,Direccion

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_de_nacimiento',
            'curp',
            'rfc',
            'direccion',
        ]
        labels = {
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'fecha_de_nacimiento': 'Fecha de Nacimiento',
            'curp': 'CURP',
            'rfc': 'RFC',
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'placeholder': 'Nombre','class': 'col-md-4 form-control'}),
            "apellido_paterno": forms.TextInput(attrs={'placeholder': 'Apellido Paterno','class': 'col-md-4 form-control'}),
            "apellido_materno": forms.TextInput(attrs={'placeholder': 'Apellido Materno','class': 'col-md-4 form-control'}),
            "fecha_de_nacimiento": forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd','type': 'text', 'id': 'datepicker', 'maxlength': '10','class': 'col-md-4 form-control'}),
            "curp": forms.TextInput(attrs={'placeholder': 'CURP','class': 'col-md-4 form-control'}),
            "rfc": forms.TextInput(attrs={'placeholder': 'RFC','class': 'col-md-4 form-control'}),
            'direccion': forms.HiddenInput(),
        }

    def clean_fecha_de_nacimiento(self):
        diccionario_limpio = self.cleaned_data
        fecha_de_nacimiento = diccionario_limpio.get('fecha_de_nacimiento')
        #Obtenemos la fecha actual y le restamos 18 años
        fecha_actual = date.today() - timedelta(days=6570)
        patron = re.compile('[\d]{4}[-]{1}[\d]{2}[-]{1}[\d]{2}')
        if not patron.match(str(fecha_de_nacimiento)):
            raise forms.ValidationError("La fecha no coincide con el formato requerido")
        elif fecha_actual < fecha_de_nacimiento:
        #if fecha_actual < fecha_de_nacimiento:
            raise forms.ValidationError("El fecha no debe ser mayor al dia de hoy y debe ser de al menos hace 18 años")
        else:
            return fecha_de_nacimiento

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'pais',
            'estado',
            'municipio',
            'ciudad',
            'calle',
            'colonia',
            'numero_interior',
            'numero_exterior',
            'codigo_postal',
            'datos_adicionales',
        ]
        labels = {
            'pais': 'Pais',
            'estado': 'Estado',
            'municipio': 'Municipio',
            'ciudad': 'Ciudad',
            'calle': 'Calle',
            'colonia': 'Colonia',
            'numero_interior': 'Num. Int',
            'numero_exterior': 'Num. Ext',
            'codigo_postal': 'Codigo Postal',
            'datos_adicionales': 'Datos adicionales',
        }
        widgets = {
            "pais": forms.TextInput(attrs={'placeholder': 'Pais','class': 'col-md-4 form-control'}),
            "estado": forms.TextInput(attrs={'placeholder': 'Estado','class': 'col-md-4 form-control'}),
            "municipio": forms.TextInput(attrs={'placeholder': 'Municipio','class': 'col-md-4 form-control'}),
            "ciudad": forms.TextInput(attrs={'placeholder': 'Ciudad','class': 'col-md-4 form-control'}),
            "calle": forms.TextInput(attrs={'placeholder': 'Calle','class': 'col-md-4 form-control'}),
            "colonia": forms.TextInput(attrs={'placeholder': 'Colonia','class': 'col-md-4 form-control'}),
            "numero_interior": forms.TextInput(attrs={'placeholder': 'Num. Int','class': 'col-md-4 form-control'}),
            "numero_exterior": forms.TextInput(attrs={'placeholder': 'Num. Ext','class': 'col-md-4 form-control'}),
            "codigo_postal": forms.TextInput(attrs={'placeholder': 'Codigo Postal','class': 'col-md-4 form-control'}),
            "datos_adicionales": forms.TextInput(attrs={'placeholder': 'Datos adicionales','class': 'col-md-4 form-control'}),
        }