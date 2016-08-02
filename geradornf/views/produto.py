from rest_framework import viewsets

from geradornf.models import Produto
from geradornf.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint API que retorna todos os Produtos
	"""
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer