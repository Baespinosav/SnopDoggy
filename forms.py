from django import forms
from django.forms import ModelForm, fields
from .models import Vehiculo, manProducto

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'imagen', 'categoria']

class ManProdForm(ModelForm):
    class Meta:
        model = manProducto
        fields = ['id', 'categoria_man', 'nombre', 'descripcion','precio', 'descuentoSub', 'descuentoOfe','imagen']


