from django.contrib import admin

from envios.models import TipoPago , MetodoPago , Envio , Item

class EnviosAdmin(admin.ModelAdmin):
	raw_id_fields  = ('cliente' ,)
	list_display = ['id_envio' , 'cliente'  , 'contador_items', 'total']


class TipoPagoAdmin(admin.ModelAdmin):

	list_display = ['tipo']	

class MetodoPagoAdmin(admin.ModelAdmin):
	list_display = ['metodo']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['id_item' , 'id_envio' , 'producto' , 'cantidad' , 'subtotal'  ]


admin.site.register (Envio , EnviosAdmin)
admin.site.register (TipoPago ,TipoPagoAdmin)
admin.site.register (MetodoPago , MetodoPagoAdmin)
admin.site.register (Item , ItemAdmin)