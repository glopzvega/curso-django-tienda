# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import os
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your models here.

class Producto(models.Model):
	nombre = models.CharField(max_length=255)
	precio = models.IntegerField(default=0)
	descripcion = models.CharField(max_length=255, default='')
	categoria = models.CharField(max_length=255, default='')
	cantidad = models.IntegerField(default=0)
	imagen = models.ImageField(upload_to='productos/imagenes', blank=True)

	def url(self):        
		if not self.imagen:
			return os.path.join('/',settings.MEDIA_URL, "default.png")	
		# 	return self.externalURL
		# else:
		return os.path.join('/',settings.MEDIA_URL, "productos/imagenes", os.path.basename(str(self.imagen)))

	def image_tag(self):
		if not self.imagen:
			return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))
		return mark_safe('<a href="{}" target="_blank"><img src="{}" width="150" height="150" /></a>'.format(self.url(), self.url()))

	image_tag.short_description = 'Imagen' 

	def __str__(self):
		return self.nombre.encode('utf-8')
		# return self.nombre.encode('ascii', errors='replace')