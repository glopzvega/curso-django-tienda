# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Venta, VentaLinea
from productos.models import Producto

from django.contrib.auth.decorators import login_required

import time
from datetime import datetime

from django.contrib.auth.models import User

def registrar(request):

	ahora = datetime.now().strftime('%Y-%m-%d')
	request.session["ahora"] = ahora

	carrito = []
	if 'carrito' in request.session:
		carrito = request.session['carrito']

	if carrito:
		user = User.objects.get(pk=request.user.id)
		row = Venta(folio='', fecha=ahora, cliente=user)
		row.save()
		row.folio = row.id
		
		total = 0
		
		if row and row.id:
			for p in carrito:
				prod = Producto.objects.get(pk=p['id'])
				subtotal = p["cantidad_carrito"] * p["precio"]
				total += subtotal
				line = VentaLinea(producto=prod, cantidad=p["cantidad_carrito"], precio=p["precio"], subtotal=subtotal, venta=row)
				line.save()
		
		row.total = total
		row.save()
		del request.session["carrito"]
		del request.session["numero"]
		del request.session["total"]

	return redirect("/productos/")