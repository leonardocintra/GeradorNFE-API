from django.contrib import admin
from geradornf.models import Emitente, Destinatario

class EmitenteAdmin(admin.ModelAdmin):
	list_display = ('nome_fantasia', 'nome_razao', )

class DestinatarioAdmin(admin.ModelAdmin):
	list_display = ('nome_razao', 'cnpj', )

admin.site.register(Emitente, EmitenteAdmin)
admin.site.register(Destinatario, DestinatarioAdmin)