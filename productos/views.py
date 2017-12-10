# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Producto
# Use Form y ModelForm
from .forms import ProductoForm, ProductoModelForm

from django.contrib.auth.decorators import login_required

@login_required
def carrito(request):

	if not request.session.has_key("carrito"):
		request.session["carrito"] = []

	empty = False
	if not request.session["carrito"]:
		empty = True

	return render(request, "productos/carrito.html", {"empty" : empty})

@login_required
def agregar_carrito(request, prod_id):

	producto = get_object_or_404(Producto, pk=prod_id)

	if not request.session.has_key("carrito"):
		request.session["carrito"] = []
		
	carrito = request.session["carrito"]
	find = False		
	
	for el in carrito:
		if el["id"] == producto.id:
			find = True

			if producto.cantidad > el["cantidad_carrito"]:
				el["cantidad_carrito"] += 1 
				el["subtotal"] = producto.precio * el["cantidad_carrito"]
			
			break

	if not find:

		prod = {
			"id" : producto.id,
			"nombre" : producto.nombre,
			"descripcion" : producto.descripcion,
			"categoria" : producto.categoria,
			"precio" : producto.precio,
			"cantidad" : producto.cantidad,
			"cantidad_carrito" : 1,
			"subtotal" : producto.precio
		}

		carrito.append(prod)

	total = 0
	for el in carrito:
		total += el["subtotal"]

	request.session["total"] = total
	request.session["carrito"] = carrito

	return redirect("/carrito/")

@login_required
def quitar_carrito(request, prod_id):

	producto = get_object_or_404(Producto, pk=prod_id)

	if not request.session.has_key("carrito"):
		request.session["carrito"] = []
		
	carrito = request.session["carrito"]	
	
	for el in carrito:
		if el["id"] == producto.id:
			carrito.remove(el)			
			break

	total = 0
	for el in carrito:
		total += el["subtotal"]

	request.session["total"] = total
	request.session["carrito"] = carrito

	return redirect("/carrito/")

@login_required
def listado(request):
	
	# Obtengo lista de productos
	lista_productos = Producto.objects.all()

	# Genero objeto que me servira como contexto para enviar al template
	data = {
		"lista" : lista_productos
	}

	# Devuelvo un template enviando el contexto
	return render(request, "productos/listado.html", data)

@login_required
def listado_cards(request):
	
	# Obtengo lista de productos
	lista_productos = Producto.objects.all()

	# Genero objeto que me servira como contexto para enviar al template
	data = {
		"lista" : lista_productos
	}

	# Devuelvo un template enviando el contexto
	return render(request, "productos/listado_cards.html", data)

@login_required
def vender(request, prod_id):
	
	# Busca un registro por primary key o devuelve un error 404 en caso
	# de no encontrar el registro
	product = get_object_or_404(Producto, pk=prod_id)

	if not request.session.get("carrito", False):
		request.session["carrito"] = []
	
	carrito = request.session["carrito"]
	find = False
	for p in carrito:
		if p["id"] == product.id:
			find = True
			p["cantidad"] = p["cantidad"] + 1

	if not find:
		carrito.append({
			"id" : product.id,
			"producto" : product.nombre,
			"cantidad" : 1
		})

	request.session["carrito"] = carrito

	# Modifico los datos del objeto obtenido
	product.cantidad = product.cantidad - 1	

	# Guardo el cambio
	product.save()

	# Guardo el objeto modificado en un diccionario para enviarlo
	# como contexto al template
	context = {
		"product" : product,		
	}

	# Devuelvo el template
	return redirect("detail", prod_id=product.id)

@login_required
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

@login_required
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

@login_required
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

@login_required
def eliminar(request, prod_id):
	producto = get_object_or_404(Producto, pk=prod_id)
	producto.delete()
	
	data = Producto.objects.all()
	return redirect('/productos/', {"lista" : data})
	# return render(request, 'productos/listado.html', {"lista" : data})

@login_required
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

