from rest_framework import viewsets

from geradornf.models import Emitente
from geradornf.serializers import EmitenteSerializer

class EmitenteViewSet(viewsets.ModelViewSet):
	"""
	Endpoint API que retorna todos os emitentes
	"""
	queryset = Emitente.objects.all()
	serializer_class = EmitenteSerializer