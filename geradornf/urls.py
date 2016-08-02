from django.conf.urls import url, include
from rest_framework import routers
from geradornf.views import emitente, produto, destinatario

router = routers.DefaultRouter()
router.register(r'emitente', emitente.EmitenteViewSet)
router.register(r'produto', produto.ProdutoViewSet)
router.register(r'destinatario', destinatario.DestinatarioViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]