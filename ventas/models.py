from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Venta(models.Model):

	folio = models.CharField(max_length=255, default='')
	cliente = models.ForeignKey(User)
	fecha = models.DateField()
	total = models.IntegerField(default=0)

	def __str__(self):
		return self.folio + " - "+ str(self.fecha) + " $" + str(self.total)

class VentaLinea(models.Model):

	producto = models.ForeignKey('productos.Producto')
	cantidad = models.IntegerField()
	precio = models.IntegerField()
	subtotal = models.IntegerField()
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.producto.nombre.encode('utf-8') + " x " + str(self.cantidad) + " $" + str(self.precio) + "= $" + str(self.subtotal)


