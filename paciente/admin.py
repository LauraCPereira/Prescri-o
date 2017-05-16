from django.contrib import admin
from paciente.models import *


class PacienteAdmin(admin.ModelAdmin):
    """
    Admin para o model Paciente
    """
    list_display = ['nome', 'data_nascimento']
    search_fields = ['nome', 'data_nascimento']
    list_filter = ['sexo']

admin.site.register(Paciente, PacienteAdmin)
