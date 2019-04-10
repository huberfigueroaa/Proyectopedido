from django.db import models

class Producto(models.Model):

	id_pro = models.AutoField(primary_key=True)
	descripcion = models.CharField('Nombre' , max_length=100)
	codigo = models.CharField('Codigo' , max_length=20)
	precio = models.DecimalField('Precio' , default=0 ,  max_digits=7 , decimal_places=2)

	def __str__ (self):
		return  self.descripcion 



