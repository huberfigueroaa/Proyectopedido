from django.urls import path, include

from envios.views import (IndexView , PedidosView
	)


urlpatterns = [
     path('' , IndexView.as_view() , name='index'),
     path('ver/pedidos'  , PedidosView.as_view() , name='ver_pedidos' )


    ]


