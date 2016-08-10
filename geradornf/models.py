from django.db import models
from .constants import UNIDADE_FEDERATIVA

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
    uf = models.CharField(max_length=2, choices=UNIDADE_FEDERATIVA)
    pais_codigo = models.IntegerField(default=1058)
    pais = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(auto_now=True)

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
    uf = models.CharField(max_length=2, choices=UNIDADE_FEDERATIVA)
    im = models.CharField(max_length=50, blank=True, null=True)
    cnae = models.CharField(max_length=50)
    pais_codigo = models.IntegerField(default=1058)
    pais = models.CharField(max_length=200, default='Brasil')
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'emitente'
        ordering = ('nome_fantasia', 'nome_razao', )


class Produto(models.Model):
    CFOP = models.IntegerField()
    EAN = models.CharField(max_length=50, blank=True, null=True)
    NCM = models.IntegerField()
    descricao = models.CharField(max_length=300)
    unidade = models.CharField(max_length=2) #fazer um choice
    valor_unitario = models.DecimalField(max_digits=9, decimal_places=2) 
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produto'
        ordering = ('descricao', )


class Transportador(models.Model):
    frete_por_conta = models.BooleanField(default=False)
    cpf_cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=20)
    nome_razao = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cidade_codigo = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=2, choices=UNIDADE_FEDERATIVA)
    cep = models.CharField(max_length=8)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'transportador'
        ordering = ('nome_razao', )


class TransportadorContrato(models.Model):
    transportador_id = models.ForeignKey(Transportador, on_delete=models.CASCADE)
    valor_servico = models.DecimalField(decimal_places=2, max_digits=9)
    valor_base = models.DecimalField(decimal_places=2, max_digits=9)
    aliquota = models.DecimalField(decimal_places=2, max_digits=9)
    valor_total = models.DecimalField(decimal_places=2, max_digits=9)
    CFOP = models.CharField(max_length=50, blank=True, null=True)
    cidade_codigo_placa = models.IntegerField(blank=True, null=True)
    RNTC = models.CharField(max_length=50, blank=True, null=True)
