# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'El pa\xc3\xads solo debe contener caracteres alfabeticos')])),
                ('estado', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'El estado solo debe contener caracteres alfabeticos')])),
                ('municipio', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'El municipio solo debe contener caracteres alfabeticos')])),
                ('ciudad', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'La ciudad solo debe contener caracteres alfabeticos')])),
                ('calle', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[[0-9a-zA]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a\xc2\xb0]]*$', message=b'La calle solo debe contener caracteres alfan\xc3\xbamericos')])),
                ('colonia', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[[0-9a-zA]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a\xc2\xb0]]*$', message=b'La colonia solo debe contener caracteres alfan\xc3\xbamericos')])),
                ('numero_interior', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[[0-9a-zA-Z]|[\xc3\xb1\xc3\x91]]*$', message=b'El numero exterior solo debe contener caracteres alfan\xc3\xbamericos')])),
                ('numero_exterior', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[[0-9a-zA-Z]|[\xc3\xb1\xc3\x91]]*$', message=b'El numero exterior solo debe contener caracteres alfan\xc3\xbamericos')])),
                ('codigo_postal', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[1-9]{1}[0-9]{4}', message=b'El codigo postal debe tener solo numeros y ademas no iniciar en un cero')])),
                ('datos_adicionales', models.CharField(blank=True, max_length=120, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[\\w]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a\xc2\xb0]*$', message=b'Los datos adicionales solo debe contener caracteres alfan\xc3\xbamericos')])),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('activo', models.IntegerField(default=1)),
                ('nombre', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'El nombre solo debe contener caracteres alfabeticos')])),
                ('apellido_paterno', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'El apellido paterno solo debe contener caracteres alfabeticos')])),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[[a-zA-Z]|[\xc3\xb1\xc3\x91\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba\xc3\x81\xc3\x89\xc3\x8d\xc3\x93\xc3\x9a]]*$', message=b'El apellido materno solo debe contener caracteres alfabeticos')])),
                ('fecha_de_nacimiento', models.DateField()),
                ('curp', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(regex=b'[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}', message=b'La CURP no tiene el formato requerido')])),
                ('rfc', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex=b'([A-Z,\xc3\x91,&]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[A-Z|\\d]{3,4})', message=b'El RFC no tiene el formato requerido')])),
                ('direccion', models.ForeignKey(blank=True, to='empleados.Direccion', null=True)),
            ],
        ),
    ]
