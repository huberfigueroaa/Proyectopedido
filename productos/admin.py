#from the django
from django.contrib import admin

#form the models
from productos.models import Producto


class ProductoAdmin(admin.ModelAdmin):

	list_display = ['id_pro' , 'descripcion' , 'codigo']


admin.site.register (Producto , ProductoAdmin)