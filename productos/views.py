# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Producto
# Use Form y ModelForm
from .forms import ProductoForm, ProductoModelForm

def listado(request):
	
	# Obtengo lista de productos
	lista_productos = Producto.objects.all()

	# Genero objeto que me servira como contexto para enviar al template
	data = {
		"lista" : lista_productos
	}

	# Devuelvo un template enviando el contexto
	return render(request, "productos/listado.html", data)

def listado_cards(request):
	
	# Obtengo lista de productos
	lista_productos = Producto.objects.all()

	# Genero objeto que me servira como contexto para enviar al template
	data = {
		"lista" : lista_productos
	}

	# Devuelvo un template enviando el contexto
	return render(request, "productos/listado_cards.html", data)

def vender(request, prod_id):
	
	# Busca un registro por primary key o devuelve un error 404 en caso
	# de no encontrar el registro
	product = get_object_or_404(Producto, pk=prod_id)

	# Modifico los datos del objeto obtenido
	product.cantidad = product.cantidad - 1	

	# Guardo el cambio
	product.save()

	# Guardo el objeto modificado en un diccionario para enviarlo
	# como contexto al template
	context = {
		"product" : product
	}

	# Devuelvo el template
	return redirect("detail", prod_id=product.id)

def comprar(request, prod_id):
	
	# Busca un registro por primary key o devuelve un error 404 en caso
	# de no encontrar el registro
	product = get_object_or_404(Producto, pk=prod_id)

	# Modifico los datos del objeto obtenido
	product.cantidad = product.cantidad + 1	

	# Guardo el cambio
	product.save()

	# Guardo el objeto modificado en un diccionario para enviarlo
	# como contexto al template
	context = {
		"product" : product
	}

	# Devuelvo el template
	return redirect("detail", prod_id=product.id)

def modificar(request, prod_id):
	
	# Obtengo un registro por pk o devuelvo un 404
	producto = get_object_or_404(Producto, pk=prod_id)
	
	# Si accedo por medio de POST a esta vista
	if request.method == 'POST':
		# Obtengo la informacion enviada por POST y FILES
		form = ProductoModelForm(request.POST, request.FILES, instance=producto)
		# Valido el formulario
		if form.is_valid():
			# Guardo el formulario
			form.save()
			# Devuelvo el template
			return render(request, 'productos/detail.html', {'product' : producto })
	
	# Si acceso por GET
	else:
		# Genero una instancia de mi ModelForm
		# Le paso como parametro el producto que voy a enviar
		form = ProductoModelForm(instance=producto)

	# Devuelvo el template
	return render(request, 'productos/producto_form.html', {'form': form, "product" : producto})

def nuevo(request):	
	
	if request.method == 'POST':
		form = ProductoModelForm(request.POST, request.FILES)
		if form.is_valid():
			
			producto = Producto()
			producto.nombre = form.cleaned_data["nombre"]
			producto.descripcion = form.cleaned_data["descripcion"]
			producto.categoria = form.cleaned_data["categoria"]
			producto.cantidad = form.cleaned_data["cantidad"]
			producto.precio = form.cleaned_data["precio"]
			producto.imagen = form.cleaned_data["imagen"]
			producto.save()
			return redirect('detail', prod_id=producto.id)
			
	else:
		form = ProductoModelForm()

	return render(request, 'productos/formulario.html', {'form': form })

def eliminar(request, prod_id):
	producto = get_object_or_404(Producto, pk=prod_id)
	producto.delete()
	
	data = Producto.objects.all()
	return redirect('/productos/', {"lista" : data})
	# return render(request, 'productos/listado.html', {"lista" : data})

def detail(request, prod_id):

	product = get_object_or_404(Producto, pk=prod_id)
	
	context = {
		"product" : product
	}
	return render(request, "productos/detail.html", context)

# def index(request):
# 	data = Producto.objects.all()
# 	context = {
# 		"data" : data 
# 	}
# 	return render(request, "productos/index.html", context)

# def detail(request, prod_id):
# 	product = get_object_or_404(Producto, pk=prod_id)
# 	context = {
# 		"product" : product
# 	}
# 	return render(request, "productos/detail.html", context)

