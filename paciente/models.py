from __future__ import unicode_literals
from django.db import models

# Create your models here

class Paciente(models.Model):
    """
    """
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    sexo = models.IntegerField(choices = ((1, "F"), (2, "M")))
    endereco = models.CharField(max_length = 250, blank= True, null = True)
    telefone = models.CharField(max_length = 12, blank= True, null = True)

    def __str__(self):
        return '{} {} {} {} {}'.format(
            self.nome,
            self.data_nascimento,
            self.get_sexo_display(),
            self.endereco,
            self.telefone
        )

class SinalVital(models.Model):
    assinatura = models.CharField(max_length = 20)
    hora = models.TimeField(auto_now_add=True)
    pa = models.BooleanField(blank= True)
    t = models.BooleanField(blank= True)
    p = models.BooleanField(blank= True)
    r = models.BooleanField(blank= True)
    eva = models.BooleanField(blank= True)
    spo2 = models.BooleanField(blank= True)
    dextro = models.BooleanField(blank= True)

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(
            self.assinatura,
            self.hora,
            self.pa,
            self.t,
            self.p,
            self.r,
            self.eva,
            self.spo2,
            self.dextro
        )


class Entrada(models.Model):
    npt = models.BooleanField(blank= True)
    ne = models.BooleanField(blank= True)

    def __str__(self):
        return '{} {}'.format(
            self.npt,
            self.ne
        )


class BalancoHidrico(models.Model):
    diurese = models.BooleanField(blank= True)
    evac = models.BooleanField(blank= True)
    dreno_d = models.BooleanField(blank= True)
    dreno_e = models.BooleanField(blank= True)
    portovack = models.BooleanField(blank= True)
    outros = models.BooleanField(blank= True)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.diurese,
            self.evac,
            self.dreno_d,
            self.dreno_e,
            self.portovack,
            self.outros
        )


class ControleEspecial(models.Model):
    avp = models.CharField(max_length=20)
    clp = models.CharField(max_length=20)
    avc = models.CharField(max_length=20)
    cdl = models.CharField(max_length=20)
    colocado_dia = models.DateField(blank= True)
    trocar_dia = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.avp,
            self.clp,
            self.avc,
            self.cdl,
            self.colocado_dia,
            self.trocar_dia
        )
