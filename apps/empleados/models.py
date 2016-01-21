# -*- encoding:UTF-8 -*-
from django.core.validators import RegexValidator
from django.db import models
# Create your models here.

class Direccion(models.Model):
    pais = models.CharField(max_length=30,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='El país solo debe contener caracteres alfabeticos'
        )
    ])
    estado = models.CharField(max_length=30,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='El estado solo debe contener caracteres alfabeticos'
        )
    ])
    municipio = models.CharField(max_length=30,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='El municipio solo debe contener caracteres alfabeticos'
        )
    ])
    ciudad = models.CharField(max_length=40, null=True, blank=True,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='La ciudad solo debe contener caracteres alfabeticos'
        )
    ])
    calle = models.CharField(max_length=40,validators=[
        RegexValidator(
            regex='^[[0-9a-zA]|[ñÑáéíóúÁÉÍÓÚ°]]*$',
            message='La calle solo debe contener caracteres alfanúmericos'
        )
    ])
    colonia = models.CharField(max_length=30, null=True, blank=True,validators=[
        RegexValidator(
            regex='^[[0-9a-zA]|[ñÑáéíóúÁÉÍÓÚ°]]*$',
            message='La colonia solo debe contener caracteres alfanúmericos'
        )
    ])
    numero_interior = models.CharField(max_length=5, null=True, blank=True,validators=[
        RegexValidator(
            regex='^[[0-9a-zA-Z]|[ñÑ]]*$',
            message='El numero exterior solo debe contener caracteres alfanúmericos'
        )
    ])
    numero_exterior = models.CharField(max_length=5, null=True, blank=True,validators=[
        RegexValidator(
            regex='^[[0-9a-zA-Z]|[ñÑ]]*$',
            message='El numero exterior solo debe contener caracteres alfanúmericos'
        )
    ])
    codigo_postal = models.CharField(max_length=5, null=True, blank=True,validators=[
        RegexValidator(
            regex='^[1-9]{1}[0-9]{4}',
            message='El codigo postal debe tener solo numeros y ademas no iniciar en un cero'
        )
    ])
    datos_adicionales = models.CharField(max_length=120, null=True, blank=True,validators=[
        RegexValidator(
            regex='^[\w]|[ñÑáéíóúÁÉÍÓÚ°]*$',
            message='Los datos adicionales solo debe contener caracteres alfanúmericos'
        )
    ])

    def get_full_information(self):
        return '%s %s %s %s %s %s %s %s %s %s' % (
            self.calle,
            self.numero_interior ,
            self.numero_exterior,
            self.datos_adicionales,
            self.colonia,
            self.municipio,
            self.ciudad,
            self.codigo_postal,
            self.estado,
            self.pais
        )

class Empleado(models.Model):
    fecha_registro= models.DateTimeField(auto_now_add=True)
    activo = models.IntegerField(default=1)
    nombre = models.CharField(max_length=100,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='El nombre solo debe contener caracteres alfabeticos',
        )
    ])
    apellido_paterno = models.CharField(max_length=50,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='El apellido paterno solo debe contener caracteres alfabeticos'
        )
    ])
    apellido_materno = models.CharField(max_length=50,null=True,blank=True,validators=[
        RegexValidator(
            regex='^[[a-zA-Z]|[ñÑáéíóúÁÉÍÓÚ]]*$',
            message='El apellido materno solo debe contener caracteres alfabeticos'
        )
    ])
    fecha_de_nacimiento = models.DateField()
    curp = models.CharField(max_length=18,validators=[
        RegexValidator(
            regex='[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}',
            message='La CURP no tiene el formato requerido'
        )
    ])
    rfc = models.CharField(max_length=14,validators=[
        RegexValidator(
            regex='([A-Z,Ñ,&]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[A-Z|\d]{3,4})',
            message='El RFC no tiene el formato requerido'
        )
    ])
    direccion = models.ForeignKey(Direccion, null=True, blank=True)#, on_delete=models.CASCADE)

    def get_estatus_display(self):
        if self.activo==1:
            return "Activo"
        else:
            return "Inactivo"

    def __unicode__(self):
        return (self.nombre)