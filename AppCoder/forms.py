from django import forms
from AppCoder.models import Canal,Productos,DatosCanal

class canalFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    campo1 = forms.CharField()
    campo2 = forms.CharField()   
    campo3 = forms.CharField()
    campo4 = forms.CharField()
    campo5 = forms.CharField()
    campo6 = forms.CharField()
    campo7 = forms.CharField()
    campo8 = forms.CharField()
    class Meta:
        model = Canal
        field = ("nombre","descripcion","campo1","campo2","campo3","campo4","campo5","campo6","campo7","campo8")

class DatosCanalFormulario(forms.Form):
    campo1 = forms.CharField()
    campo2 = forms.CharField()   
    campo3 = forms.CharField()
    campo4 = forms.CharField()
    campo5 = forms.CharField()
    campo6 = forms.CharField()
    campo7 = forms.CharField()
    campo8 = forms.CharField()
    class Meta:
        model = DatosCanal
        field = ("campo1","campo2","campo3","campo4","campo5","campo6","campo7","campo8")


class ProductosFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.CharField()
    class Meta:
        model = Productos
        field = ("nombre","descripcion","precio")