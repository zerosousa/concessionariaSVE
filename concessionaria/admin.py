from django.contrib import admin
from django.db import IntegrityError
from django.db.models import Sum

# Register your models here.
from .models import *

class BairroAdmin(admin.ModelAdmin):
    list_display = ['nm_bairro']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(BairroAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(BairroAdmin, self).changelist_view(request, extra_context)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nm_cidade']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(CidadeAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(CidadeAdmin, self).changelist_view(request, extra_context)
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nm_cliente']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(ClienteAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(ClienteAdmin, self).changelist_view(request, extra_context)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cd_cep', 'nu_numero', 'de_complemento']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(EnderecoAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(EnderecoAdmin, self).changelist_view(request, extra_context)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nm_funcionario']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(FuncionarioAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(FuncionarioAdmin, self).changelist_view(request, extra_context)

class LocalAdmin(admin.ModelAdmin):
    list_display = ['de_local']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(LocalAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(LocalAdmin, self).changelist_view(request, extra_context)

class LogradouroAdmin(admin.ModelAdmin):
    list_display = ['nm_logradouro']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(LogradouroAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(LogradouroAdmin, self).changelist_view(request, extra_context)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['de_marca']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(MarcaAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(MarcaAdmin, self).changelist_view(request, extra_context)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ['de_modelo']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(ModeloAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(ModeloAdmin, self).changelist_view(request, extra_context)

class MotoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'cd_chassi']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(MotoAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(MotoAdmin, self).changelist_view(request, extra_context)

class OrdemservicoAdmin(admin.ModelAdmin):
    list_display = ['dt_ordem']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(OrdemservicoAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(OrdemservicoAdmin, self).changelist_view(request, extra_context)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['de_produto']

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['de_servico']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(ServicoAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(ServicoAdmin, self).changelist_view(request, extra_context)

class ServicoporordemAdmin(admin.ModelAdmin):
    list_display = ['numero_ordem', 'moto_chassi', 'moto_placa']

    def moto_chassi(self, instance):
        return instance.ordemservico.moto.cd_chassi

    def moto_placa(self, instance):
        return instance.ordemservico.moto.placa

    def numero_ordem(self, instance):
        return instance.ordemservico.nu_ordem
  
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['dt_data']

class UfAdmin(admin.ModelAdmin):
    list_display = ['nm_uf']

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super(UfAdmin, self).delete_view(request, object_id, extra_context)
        except (IntegrityError) as e:
            request.method = 'GET'
            messages.error(request, e.message)
            return super(UfAdmin, self).changelist_view(request, extra_context)

class NfDetalhadaAdmin(admin.ModelAdmin):
    list_display = ['numero_ordem', 'moto_chassi', 'moto_placa', 'sum_valor']

    def moto_chassi(self, instance):
        return instance.ordemservico.moto.cd_chassi

    def moto_placa(self, instance):
        return instance.ordemservico.moto.placa

    def numero_ordem(self, instance):
        return instance.ordemservico.nu_ordem

class MotoDetalhadaAdmin(admin.ModelAdmin):
    list_display = ['moto_chassi',
                    'moto_placa',
                    'moto_marca',
                    'moto_modelo',
                    'moto_cor',
                    'moto_ano_fabricacao',
                    'moto_cilindradas',
                    'moto_local']

    def moto_chassi(self, instance):
        return instance.moto.cd_chassi

    def moto_placa(self, instance):
        return instance.moto.placa

    def moto_marca(self, instance):
        return instance.moto.id_modelo.id_marca.de_marca

    def moto_modelo(self, instance):
        return instance.moto.id_modelo.de_modelo

    def moto_cor(self, instance):
        return instance.moto.cor

    def moto_ano_fabricacao(self, instance):
        return instance.moto.ano_fabricacao

    def moto_cilindradas(self, instance):
        return instance.moto.id_modelo.nu_cilindradas

    def moto_local(self, instance):
        return instance.moto.id_local.de_local

class ClienteDetalhadoAdmin(admin.ModelAdmin):
    list_display = ['cliente_cpf',
                    'cliente_nome',
                    'cliente_telefone',
                    'logradouro',
                    'numero',
                    'bairro',
                    'cep',
                    'cidade',
                    'uf',
                    'cd_chassi',
                    'de_marca',
                    'de_modelo',
                    'cor',
                    'ano_fabricacao',
                    'nu_cilindradas',
                    'placa',
                    'de_local']

    def cliente_cpf(self, instance):
        return instance.cliente.cd_cpfcliente

    def cliente_nome(self, instance):
        return instance.cliente.nm_cliente

    def cliente_telefone(self, instance):
        return instance.cliente.nu_telefone

    def logradouro(self, instance):
        return instance.cliente.id_endereco.id_logradouro.nm_logradouro

    def numero(self, instance):
        return instance.cliente.id_endereco.nu_numero

    def bairro(self, instance):
        return instance.cliente.id_endereco.id_logradouro.id_bairro.nm_bairro

    def cep(self, instance):
        return instance.cliente.id_endereco.cd_cep

    def cidade(self, instance):
        return instance.cliente.id_endereco.id_logradouro.id_bairro.id_cidade.nm_cidade

    def uf(self, instance):
        return instance.cliente.id_endereco.id_logradouro.id_bairro.id_cidade.cd_uf.nm_uf

admin.site.register(Bairro, BairroAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Logradouro, LogradouroAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Moto, MotoAdmin)
admin.site.register(Ordemservico, OrdemservicoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Servicoporordem, ServicoporordemAdmin)
admin.site.register(Transacao, TransacaoAdmin)
admin.site.register(Uf, UfAdmin)
admin.site.register(NfDetalhada, NfDetalhadaAdmin)
admin.site.register(MotoDetalhada, MotoDetalhadaAdmin)
admin.site.register(ClienteDetalhado, ClienteDetalhadoAdmin)
