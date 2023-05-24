from django.db import models

# Criando os modolos do meu crud

# criar a class do meu modolo e as especificacao do mesmo
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    trabalho = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome
    
