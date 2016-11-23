from django.contrib import admin

# Register your models here.
from .models import *

class MotoAdmin(admin.ModelAdmin):
    list_display = ('placa')

admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Funcionario)
admin.site.register(Local)
admin.site.register(Logradouro)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Moto, MotoAdmin)
admin.site.register(Ordemservico)
admin.site.register(Produto)
admin.site.register(Servico)
admin.site.register(Servicoporordem)
admin.site.register(Transacao)
admin.site.register(Uf)
