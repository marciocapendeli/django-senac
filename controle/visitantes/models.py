from django.db import models

# Create your models here.

class Visitante(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  # CPF pode ter 11 números, com ou sem pontos e hífens
    data_nascimento = models.DateField()
    numero_casa = models.CharField(max_length=10)
    placa_veiculo = models.CharField(max_length=10)
    hora_chegada = models.TimeField()
    hora_saida = models.TimeField()
    hora_autorizacao = models.TimeField()
    nome_morador = models.CharField(max_length=100)
    porteiro_autorizou = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo
