from rest_framework import serializers
from CRUD.models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    """Pessoas"""
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'trabalho']
