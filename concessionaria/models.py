from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

class Transac(models.Field):
    def db_type(self, connection):
        return 'transac'

class Bairro(models.Model):
    id_bairro = models.AutoField(primary_key=True)
    nm_bairro = models.CharField(max_length=1000, blank=True, null=True)
    id_cidade = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='id_cidade', blank=True, null=True)

    def __str__(self):
        return self.nm_bairro
    
    class Meta:
        db_table = 'bairro'


class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nm_cidade = models.CharField(max_length=1000, blank=True, null=True)
    cd_uf = models.ForeignKey('Uf', models.DO_NOTHING, db_column='cd_uf', blank=True, null=True)

    def __str__(self):
        return self.nm_cidade

    class Meta:
        db_table = 'cidade'


class Cliente(models.Model):
    cd_cpfcliente = models.CharField(primary_key=True, max_length=11)
    nm_cliente = models.CharField(max_length=1000, blank=True, null=True)
    nu_telefone = models.CharField(max_length=1000, blank=True, null=True)
    id_endereco = models.ForeignKey('Endereco', models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)

    def __str__(self):
        return self.cd_cpfcliente

    class Meta:
        db_table = 'cliente'

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    nu_numero = models.CharField(max_length=1000, blank=True, null=True)
    cd_cep = models.CharField(max_length=1000, blank=True, null=True)
    de_complemento = models.CharField(max_length=1000, blank=True, null=True)
    id_logradouro = models.ForeignKey('Logradouro', models.DO_NOTHING, db_column='id_logradouro', blank=True, null=True)

    def __str__(self):
        return self.id_endereco

    class Meta:
        db_table = 'endereco'


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nm_funcionario = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nm_funcionario

    class Meta:
        db_table = 'funcionario'


class Local(models.Model):
    id_local = models.AutoField(primary_key=True)
    de_local = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.de_local

    class Meta:
        db_table = 'local'


class Logradouro(models.Model):
    id_logradouro = models.AutoField(primary_key=True)
    nm_logradouro = models.CharField(max_length=1000, blank=True, null=True)
    id_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='id_bairro', blank=True, null=True)

    def __str__(self):
        return self.nm_logradouro

    class Meta:
        db_table = 'logradouro'


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    de_marca = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.de_marca

    class Meta:
        db_table = 'marca'


class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    de_modelo = models.CharField(max_length=1000, blank=True, null=True)
    id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    nu_ano = models.BigIntegerField(blank=True, null=True)
    nu_cilindradas = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.de_modelo

    class Meta:
        db_table = 'modelo'


class Moto(models.Model):
    cd_chassi = models.CharField(primary_key=True, max_length=1000)
    placa = models.CharField(max_length=1000, blank=True, null=True)
    cor = models.CharField(max_length=1000, blank=True, null=True)
    ano_fabricacao = models.CharField(max_length=1000, blank=True, null=True)
    id_local = models.ForeignKey(Local, models.DO_NOTHING, db_column='id_local', blank=True, null=True)
    id_modelo = models.ForeignKey(Modelo, models.DO_NOTHING, db_column='id_modelo', blank=True, null=True)

    def __str__(self):
        return self.cd_chassi
        
    class Meta:
        db_table = 'moto'


class Ordemservico(models.Model):
    nu_ordem = models.AutoField(primary_key=True)
    cd_cpfcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cd_cpfcliente', blank=True, null=True)
    dt_ordem = models.CharField(max_length=1000, blank=True, null=True)
    cd_chassi = models.ForeignKey(Moto, models.DO_NOTHING, db_column='cd_chassi', blank=True, null=True)
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='id_funcionario', blank=True, null=True)

    def __str__(self):
        return '%s ; %s ; %s ; %s' % (self.nu_ordem, self.cd_cpfcliente, self.dt_ordem, self.cd_chassi)

    class Meta:
        db_table = 'ordemservico'


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    de_produto = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.de_produto

    class Meta:
        db_table = 'produto'


class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    de_servico = models.CharField(max_length=1000, blank=True, null=True)
    nu_valor = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.de_servico

    class Meta:
        db_table = 'servico'


class Servicoporordem(models.Model):
    id_servico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='id_servico')
    nu_ordem = models.ForeignKey(Ordemservico, models.DO_NOTHING, db_column='nu_ordem')
    id_funcionario = models.CharField(max_length=1000, blank=True, null=True)
    id_produto = models.BigIntegerField(blank=True, null=True)
    nu_quantidade = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return '%s ; %s' % (self.id_servico, self.nu_ordem)

    class Meta:
        db_table = 'servicoporordem'
        verbose_name = "Nf detalhada"
        verbose_name_plural = "Nf detalhadas"
        unique_together = (('id_servico', 'nu_ordem'),)


class Transacao(models.Model):
    id_notafiscal = models.CharField(primary_key=True, max_length=1000)
    dt_data = models.CharField(max_length=1000, blank=True, null=True)
    tp_transacao = Transac(blank=True, null=True)
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='id_funcionario', blank=True, null=True)
    cd_chassi = models.ForeignKey(Moto, models.DO_NOTHING, db_column='cd_chassi', blank=True, null=True)
    cd_cpfcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cd_cpfcliente', blank=True, null=True)

    def __str__(self):
        return '%s ; %s ; %s' % (self.tp_transacao, self.dt_data, self.cd_cpfcliente)

    class Meta:
        db_table = 'transacao'


class Uf(models.Model):
    cd_uf = models.CharField(primary_key=True, max_length=1000)
    nm_uf = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nm_uf

    class Meta:
        db_table = 'uf'
