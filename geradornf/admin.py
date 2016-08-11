from django.contrib import admin
from geradornf.models import Emitente, Destinatario, Cliente

class EmitenteAdmin(admin.ModelAdmin):
	list_display = ('nome_fantasia', 'nome_razao', )

class DestinatarioAdmin(admin.ModelAdmin):
	list_display = ('nome_razao', 'cnpj', )

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email')

admin.site.register(Emitente, EmitenteAdmin)
admin.site.register(Destinatario, DestinatarioAdmin)
admin.site.register(Cliente, ClienteAdmin)