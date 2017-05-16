from django.db import models
from paciente.models import Paciente


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(
            self.nome
        )

class Ala(models.Model):
    codigo_ala = models.CharField(max_length=5)

    def __str__(self):
        return '{}'.format(
            self.codigo_ala
        )


class Leito(models.Model):
    codigo_leito = models.CharField(max_length=5)

    def __str__(self):
        return '{}'.format(
            self.codigo_leito
        )

class PrescricaoEnfermagem(models.Model):
    paciente = models.ForeignKey(Paciente)
    leito = models.ForeignKey(Leito)
    especialidade = models.ForeignKey(Especialidade)
    data = models.DateField(auto_now_add=True)
    ala = models.ForeignKey(Ala)


    def __str__(self):
        return '{} {} {} {} {}'.format(
            self.paciente,
            self.leito,
            self.especialidade,
            self.data,
            self.ala
        )
