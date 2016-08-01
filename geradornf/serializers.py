from rest_framework import serializers
from geradornf.models import Emitente

class EmitenteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Emitente
		fields = ('id', 'url', 'cnpj', 'inscricao_estadual', 'nome_razao', 'nome_fantasia', 'data_cadastro', \
				'fone', 'cep', 'logradouro', 'numero_casa', 'complemento', 'bairro', 'cidade_codigo', 'cidade', \
				'uf', 'im', 'cnae', 'pais_codigo', 'pais', 
			)
