from django.shortcuts import render
from django.views.generic import DetailView , ListView


from clientes.models import Cliente


class ClienteList(ListView):
	template_name = 'clientes/lista.html'
	model = Cliente

	def get_context_data(self , *args , **kwargs):
		clientes = Cliente.objects.all()
		return {"clientes" : clientes}


