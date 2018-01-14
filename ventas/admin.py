# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Venta, VentaLinea
# Register your models here.

@admin.register(Venta)
class AdminVenta(admin.ModelAdmin):
	list_display = ('id', 'folio', 'cliente', 'fecha')

@admin.register(VentaLinea)
class AdminVentaLinea(admin.ModelAdmin):
	list_display = ('id', 'venta', 'producto', 'precio', 'cantidad', 'subtotal')