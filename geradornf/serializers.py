from rest_framework import serializers
from geradornf.models import Emitente, Produto, Destinatario, Transportador, Cliente


class EmitenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emitente
        fields = ('id', 'url', 'cnpj', 'inscricao_estadual', 'nome_razao', 'nome_fantasia', 'data_cadastro', \
                'fone', 'cep', 'logradouro', 'numero_casa', 'complemento', 'bairro', 'cidade_codigo', 'cidade', \
                'uf', 'im', 'cnae', 'pais_codigo', 'pais', 'cliente',
        )


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'url', 'descricao', 'CFOP', 'EAN', 'NCM', 'unidade', 'valor_unitario', 'data_cadastro', 'cliente', )


class DestinatarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destinatario
        fields = ('id', 'url', 'nome_razao', 'cnpj', 'indicador_ie_destinatario', 'inscricao_estadual', 'isuf', \
                'fone', 'cep', 'logradouro', 'numero_casa', 'complemento', 'bairro', 'cidade_codigo', 'cidade', \
                'uf', 'pais_codigo', 'pais', 'email', 'data_cadastro', 'cliente',
        )


class TransportadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transportador
        fields = ('id', 'url', 'nome_razao', 'cpf_cnpj', 'inscricao_estadual', 'endereco', 'cidade_codigo', \
                 'cidade', 'uf', 'cep', 'data_cadastro', 'cliente',
        )


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'url', 'nome', 'email')