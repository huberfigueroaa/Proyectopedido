from django.db import models

# Create your models here.



class Cliente(models.Model):

	TIPOCLIENTE = (
			('Min' , 'Minorista'),
			('May' , 'Mayorista'),
		)


	id_cliente = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre' , max_length=50)
	empresa = models.CharField('Empresa' , max_length=50)
	direccion = models.CharField('Direccion' , max_length=50)
	telefono = models.CharField('Telefono' , max_length=12)
	nit = models.CharField('Nit' , default='C/F' , max_length=9)
	email = models.EmailField('Correo Electronico' , max_length=75)
	tipo = models.CharField('Tipo de Cliente' , max_length=10 , choices=TIPOCLIENTE)


	def __str__ (self):
		return "%s" % (self.nombre)