# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_diplay = ("id", "nombre", "apellidop", "apellidom", "email")
