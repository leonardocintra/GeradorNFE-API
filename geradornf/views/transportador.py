from rest_framework import viewsets

from geradornf.models import Transportador
from geradornf.serializers import TransportadorSerializer

class TransportadorViewSet(viewsets.ModelViewSet):
	"""
	Endpoint API que retorna todos os Transportadores
	"""
	queryset = Transportador.objects.all()
	serializer_class = TransportadorSerializer