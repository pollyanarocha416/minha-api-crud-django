from django.contrib import admin
from CRUD.models import Pessoa
# Register your models here

class Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'trabalho')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Pessoa, Pessoas)
