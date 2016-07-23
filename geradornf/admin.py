from django.contrib import admin
from geradornf.models import Emitente

class EmitenteAdmin(admin.ModelAdmin):
	list_display = ('nome_fantasia', 'nome_razao', )

admin.site.register(Emitente, EmitenteAdmin)