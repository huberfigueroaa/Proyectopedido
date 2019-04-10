from django.db import models


#from models 
from clientes.models import Cliente
from productos.models import Producto


class TipoPago(models.Model):
	tipo = models.CharField('Tipo de Pago' , max_length=10)

	def __str__ (self):
		return self.tipo


class MetodoPago(models.Model):
	metodo = models.CharField('Metodo de Pago' , max_length=15)

	def __str__ (self):
		return self.metodo

class Envio(models.Model):

	id_envio = models.AutoField(primary_key=True)
	tipo = models.ForeignKey (TipoPago , on_delete=models.CASCADE)
	cliente = models.ForeignKey (Cliente , on_delete=models.CASCADE)
	metodo = models.ForeignKey (MetodoPago , on_delete=models.CASCADE)

	def __str__ (self):
		return "%s %s" % (self.id_envio , self.cliente)

	def total(self):
		items = Item.objects.filter(id_envio=self.id_envio)
		total = 0
		for item in items:
			cantidad = item.cantidad
			valor = item.producto.precio
			subtotal = cantidad * valor
			total +=subtotal
		return total

	def contador_items(self):
		cant = Item.objects.filter(id_envio=self.id_envio).count()
		return cant


class Item(models.Model):
	id_item = models.AutoField(primary_key=True)
	id_envio = models.ForeignKey(Envio , on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto , on_delete=models.CASCADE)
	cantidad = models.IntegerField('Cantidad' , default=0)


	def subtotal(self):

		cantidad = self.cantidad
		precio = self.producto.precio
		sub_total = cantidad * precio
		return sub_total

