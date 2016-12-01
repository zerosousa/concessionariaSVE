from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from django_pgviews import view as pg

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


class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    de_servico = models.CharField(max_length=1000, blank=True, null=True)
    nu_valor = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.de_servico

    class Meta:
        db_table = 'servico'


class Ordemservico(models.Model):
    nu_ordem = models.AutoField(primary_key=True)
    cd_cpfcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cd_cpfcliente', blank=True, null=True)
    dt_ordem = models.CharField(max_length=1000, blank=True, null=True)
    moto = models.ForeignKey(Moto, models.DO_NOTHING, db_column='cd_chassi', blank=True, null=True)
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='id_funcionario', blank=True, null=True)
    servicos = models.ManyToManyField(Servico, through='Servicoporordem')

    def __str__(self):
        return '%s ; %s ; %s ; %s' % (self.nu_ordem, self.cd_cpfcliente, self.dt_ordem, self.moto)

    class Meta:
        db_table = 'ordemservico'


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    de_produto = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.de_produto

    class Meta:
        db_table = 'produto'


class Servicoporordem(models.Model):
    id_servicoporordem = models.AutoField(primary_key=True)
    servico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='id_servico')
    ordemservico = models.ForeignKey(Ordemservico, models.DO_NOTHING, db_column='nu_ordem')
    funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='id_funcionario')
    produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='id_produto')
    nu_quantidade = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return '%s ; %s' % (self.servico, self.ordemservico)

    class Meta:
        db_table = 'servicoporordem'
        unique_together = (('servico', 'ordemservico'),)


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

class NfDetalhada(pg.View):
    ordemservico = models.ForeignKey(Ordemservico, models.DO_NOTHING, primary_key=True, db_column='nu_ordem')
    sum_valor = models.BigIntegerField(blank=True, null=True, db_column='sum')
    projection = ['concessionaria.Moto.cd_chassi', 'concessionaria.Moto.placa', 'concessionaria.Ordemservico.nu_ordem', 'concessionaria.Servico.nu_valor']
    sql = """SELECT mo.cd_chassi, mo.placa, os.nu_ordem, sum(se.nu_valor)
               FROM MOTO mo
               JOIN ORDEMSERVICO os ON (mo.cd_chassi = os.cd_chassi)
               JOIN ServicoPorOrdem so ON (os.nu_ordem = so.nu_ordem)
               JOIN servico se ON (so.id_servico = se.id_servico)
               GROUP BY 1, 2, 3;"""

    class Meta:
      app_label = 'concessionaria'
      db_table = 'vw_nf_detalhada'
      managed = False

class MotoDetalhada(pg.View):
    moto = models.ForeignKey(Moto, models.DO_NOTHING, primary_key=True, db_column='cd_chassi')
    projection = ['concessionaria.Moto.cd_chassi',
                  'concessionaria.Marca.de_marca',
                  'concessionaria.Modelo.de_modelo',
                  'concessionaria.Moto.cor',
                  'concessionaria.Moto.ano_fabricacao',
                  'concessionaria.Modelo.nu_cilindradas',
                  'concessionaria.Moto.placa',
                  'concessionaria.Local.de_local']
    sql = """SELECT mo.cd_chassi, ma.de_marca, ml.de_modelo, mo.cor, mo.ano_fabricacao, ml.nu_cilindradas, mo.placa, lo.de_local
               FROM MOTO mo
               JOIN modelo ml on (mo.id_modelo = ml.id_modelo)
               JOIN marca ma on (ml.id_marca = ma.id_marca)
               JOIN local lo on (mo.id_local = lo.id_local);"""

    class Meta:
      app_label = 'concessionaria'
      db_table = 'vw_moto_detalhada'
      managed = False

class ClienteDetalhado(pg.View):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, primary_key=True, db_column='cd_cpfcliente')
    cd_chassi = models.CharField(max_length=1000, blank=True, null=True, db_column='cd_chassi')
    de_marca = models.CharField(max_length=1000, blank=True, null=True, db_column='de_marca')
    de_modelo = models.CharField(max_length=1000, blank=True, null=True, db_column='de_modelo')
    cor = models.CharField(max_length=1000, blank=True, null=True, db_column='cor')
    ano_fabricacao = models.CharField(max_length=1000, blank=True, null=True, db_column='ano_fabricacao')
    nu_cilindradas = models.BigIntegerField(blank=True, null=True, db_column='nu_cilindradas')
    placa = models.CharField(max_length=1000, blank=True, null=True, db_column='placa')
    de_local = models.CharField(max_length=1000, blank=True, null=True, db_column='de_local')
    projection = ['concessionaria.Cliente.cd_cpfcliente',
                  'concessionaria.Cliente.nm_cliente',
                  'concessionaria.Cliente.nu_telefone',
                  'concessionaria.Logradouro.nm_logradouro',
                  'concessionaria.Endereco.nu_numero',
                  'concessionaria.Bairro.nm_bairro',
                  'concessionaria.Endereco.cd_cep',
                  'concessionaria.Cidade.nm_cidade',
                  'concessionaria.Uf.nm_uf',
                  'concessionaria.Moto.cd_chassi',
                  'concessionaria.Marca.de_marca',
                  'concessionaria.Modelo.de_modelo',
                  'concessionaria.Moto.cor',
                  'concessionaria.Moto.ano_fabricacao',
                  'concessionaria.Modelo.nu_cilindradas',
                  'concessionaria.Moto.placa',
                  'concessionaria.Local.de_local']
    sql = """SELECT cl.cd_cpfCliente, cl.nm_cliente, cl.nu_telefone, lg.nm_logradouro, en.nu_numero, ba.nm_bairro, en.cd_cep, ci.nm_cidade, uf.nm_uf, mo.cd_chassi, ma.de_marca, ml.de_modelo, mo.cor, mo.ano_fabricacao, ml.nu_cilindradas, mo.placa, lo.de_local
               FROM CLIENTE cl
               LEFT JOIN ENDERECO en on (cl.id_endereco = en.id_endereco)
               LEFT JOIN LOGRADOURO lg on (en.id_logradouro = lg.id_logradouro)
               LEFT JOIN BAIRRO ba on (lg.id_bairro = ba.id_bairro)
               LEFT JOIN CIDADE ci on (ba.id_cidade = ci.id_cidade)
               LEFT JOIN UF uf on (ci.cd_uf = uf.cd_uf)
               LEFT JOIN ORDEMSERVICO os on (cl.cd_cpfCliente = os.cd_cpfCliente)
               LEFT JOIN MOTO mo on (os.cd_chassi = mo.cd_chassi)
               LEFT JOIN MODELO ml on (mo.id_modelo = ml.id_modelo)
               LEFT JOIN MARCA ma on (ml.id_marca = ma.id_marca)
               LEFT JOIN local lo on (mo.id_local = lo.id_local);"""

    class Meta:
      app_label = 'concessionaria'
      db_table = 'vw_cliente_detalhado'
      managed = False
      
