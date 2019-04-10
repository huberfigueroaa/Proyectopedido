from django.shortcuts import render
from django.views.generic import TemplateView

from envios.models import Envio



class IndexView(TemplateView):

	template_name = 'envios/index.html'

class PedidosView(TemplateView):
	template_name = 'envios/pedidos.html'

	def get_context_data(self , *args , **kwargs):

		pedidos = Envio.objects.all()

		return {'pedidos' : pedidos }