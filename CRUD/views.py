from django.http import JsonResponse
from rest_framework import viewsets
from CRUD.models import Pessoa
from CRUD.serializer import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    """Exibir pessoas"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

