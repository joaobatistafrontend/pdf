from django.contrib import admin
from .models import Agenda, Local, Opcoes

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'locais', 'produtos', 'horario')

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'endereco', 'bairro', 'telefone', 'numeracao', 'mapa_link', 'logradouro')

@admin.register(Opcoes)
class OpcoesAdmin(admin.ModelAdmin):
    list_display = ('opcoes', 'valor')