from django.conf.urls import url, include
from rest_framework import routers
from geradornf.views import emitente, produto

router = routers.DefaultRouter()
router.register(r'emitente', emitente.EmitenteViewSet)
router.register(r'produto', produto.ProdutoViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]