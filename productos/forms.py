from django import forms
from django.forms import ModelForm, NumberInput, TextInput, Textarea

from .models import Producto

class ProductoModelForm(ModelForm):
	class Meta:
		model = Producto
		fields = "__all__" #("precio",)
		exlude = ("imagen",)
		widgets = {
			# 'descripcion' : Textarea(attrs={'cols':80, 'rows':5}),
            'precio': NumberInput(attrs={'min': 0}), 
            'cantidad': NumberInput(attrs={'min': 0}),            
        }

class ProductoForm(forms.Form):
	nombre = forms.CharField(label='Nombre del Producto', max_length=255)
	precio = forms.IntegerField(min_value=0, max_value=10)
	descripcion = forms.CharField(label='Descripcion del Producto', max_length=255)
	categoria = forms.CharField(label='Categoria del producto', max_length=255)
	cantidad = forms.IntegerField()
	imagen = forms.ImageField(required=False)
