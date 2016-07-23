from django.db import models

class Destinatario(models.Model):
    cnpj = models.CharField(max_length=14)
    indicador_ie_destinatario = models.IntegerField(null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=20)
    isuf = models.CharField(max_length=50, blank=True, null=True)
    nome_razao = models.CharField(max_length=200)
    fone = models.CharField(max_length=13, null=True, blank=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero_casa = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=200)
    cidade_codigo = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    pais_codigo = models.IntegerField(default=1058)
    pais = models.CharField(max_length=200)

    class Meta:
        db_table = 'destinatario'
        ordering = ('nome_razao', )


class Emitente(models.Model):
	cnpj = models.CharField(max_length=14)
	inscricao_estadual = models.CharField(max_length=20)
    nome_razao = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200)
    fone = models.CharField(max_length=13, null=True, blank=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero_casa = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=200)
    cidade_codigo = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    im = models.CharField(max_length=50)
    cnae = models.CharField(max_length=50)
    pais_codigo = models.IntegerField(default=1058)
    pais = models.CharField(max_length=200)


	class Meta:
		db_table = 'emitente'
		ordering = ('nome_fantasia', 'nome_razao', )
