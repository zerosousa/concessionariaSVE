from django.contrib import admin

# Register your models here.
from .models import *

class BairroAdmin(admin.ModelAdmin):
    list_display = ['nm_bairro']

class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nm_cidade']
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nm_cliente']

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cd_cep', 'nu_numero', 'de_complemento']

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nm_funcionario']

class LocalAdmin(admin.ModelAdmin):
    list_display = ['de_local']

class LogradouroAdmin(admin.ModelAdmin):
    list_display = ['nm_logradouro']

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['de_marca']

class ModeloAdmin(admin.ModelAdmin):
    list_display = ['de_modelo']

    def add_view(self, request, form_url='', extra_context=None):
        try:
            return super(ModeloAdmin, self).add_view(request, form_url, extra_context)
        except (IntegrityError, DatabaseError) as e:

            request.method = 'GET'
            messages.error(request, e.message)
            return super(ModeloAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            return super(ModeloAdmin, self).change_view(request, object_id, form_url, extra_context)
        except (IntegrityError, DatabaseError) as e:

            request.method = 'GET'
            messages.error(request, e.message)
            return super(ModeloAdmin, self).change_view(request, object_id, form_url, extra_context)
    # def has_delete_permission(self, request, obj=None):
    #     return False


class MotoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'cd_chassi']

class OrdemservicoAdmin(admin.ModelAdmin):
    list_display = ['dt_ordem']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['de_produto']

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['de_servico']

class ServicoporordemAdmin(admin.ModelAdmin):
    list_display = ['nu_quantidade']

class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['dt_data']

class UfAdmin(admin.ModelAdmin):
    list_display = ['nm_uf']

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
