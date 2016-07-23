from rest_framework import serializers
from geradornf.models import Emitente

class EmitenteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Emitente
