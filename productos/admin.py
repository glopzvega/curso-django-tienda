# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Producto
# Register your models here.
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'descripcion', 'categoria', 'precio', 'cantidad', 'image_tag')
