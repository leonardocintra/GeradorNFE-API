from rest_framework import viewsets

from geradornf.models import Cliente
from geradornf.serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	"""
	Endpoint API que retorna todos os Clientes
	"""
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer