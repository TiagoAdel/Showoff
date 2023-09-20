from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Recurso

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','criado', 'modificado', 'ativo')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','criado', 'icone', 'modificado', 'ativo')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo','criado','modificado', 'ativo')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso','criado', 'icone', 'modificado', 'ativo')