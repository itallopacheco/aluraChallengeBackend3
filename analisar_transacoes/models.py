from django.db import models

class Transacao(models.Model):
    bancoOrigem = models.CharField(max_length=150, verbose_name='Banco de Origem')
    agenciaOrigem = models.CharField(max_length=3, verbose_name='Agencia de Origem')
    contaOrigem = models.CharField(max_length=7, verbose_name='Conta de Origem')
    bancoDestino = models.CharField(max_length=150, verbose_name='Banco de Destino')
    agenciaDestino = models.CharField(max_length=3, verbose_name='Agencia de Destino')
    contaDestino = models.CharField(max_length=7, verbose_name='Conta de Destino')
    valorTransacao = models.DecimalField(max_length=None, max_digits=2, decimal_places=2)
    dataHora = models.DateTimeField(auto_now=False, auto_now_add=False)
