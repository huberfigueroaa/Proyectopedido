from django.contrib import admin

# Register your models here.
from clientes.models import Cliente

class ClientesAdmin(admin.ModelAdmin):

	list_display = ['nombre' , 'empresa' , 'direccion' ,'email' ,'tipo']


admin.site.register (Cliente, ClientesAdmin)