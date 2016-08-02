from rest_framework import viewsets

from geradornf.models import Destinatario
from geradornf.serializers import DestinatarioSerializer

class DestinatarioViewSet(viewsets.ModelViewSet):
	"""
	Endpoint API que retorna todos os Destinatarios
	"""
	queryset = Destinatario.objects.all()
	serializer_class = DestinatarioSerializer