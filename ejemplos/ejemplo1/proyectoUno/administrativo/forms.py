from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Estudiante, \
        NumeroTelefonico

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese nombreeeee'),
            'apellido': _('Ingrese apellido por favor'),
            'cedula': _('Ingrese cédula por favor'),
            'correo': _('Ingrese correo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        valor = "René"
        ["René"] # 1
        len( ["René"])
        """

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_correo(self):
        valor = self.cleaned_data['correo']
        if "@" not in valor or "utpl.edu.ec" or "gmail.com" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad o Gmail")
        return valor


class NumeroTelefonicoForm(ModelForm):
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']
        labels = {
            'telefono': _('Ingrese su telefono'),
            'tipo': _('Ingrese el tipo del telefono'),
        }
    def clean_telefono(self):
        valor = self.cleaned_data['telefono']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese su telefono de 10 dígitos")
        return valor

    def clean_tipo(self):
        valor = self.cleaned_data['tipo']
        if "privado" not in valor or "publico" not in valor:
            raise forms.ValidationError("Ingrese un tipo valido privado o publico")
        return valor



class NumeroTelefonicoEstudianteForm(ModelForm):

    def __init__(self, estudiante, *args, **kwargs):
        super(NumeroTelefonicoEstudianteForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        print(estudiante)

    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']
