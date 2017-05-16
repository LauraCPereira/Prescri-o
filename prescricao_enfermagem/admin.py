from django.contrib import admin
from prescricao_enfermagem.models import *
from paciente.models import Paciente, SinalVital

class EspecialidadeAdmin(admin.ModelAdmin):
    """
    Admin para o model Especialidade
    """
    list_display = ['nome']
    search_fields = ['nome']


class AlaAdmin(admin.ModelAdmin):
    """
    Admin para o model Ala
    """
    list_display = ['codigo_ala']
    search_fields = ['codigo_ala']

class LeitoAdmin(admin.ModelAdmin):
    """
    Admin para o model Leito
    """
    list_display = ['codigo_leito']
    search_fields = ['codigo_leito']

class PrescricaoEnfermagemAdmin(admin.ModelAdmin):
    """
    Admin para o model PrescricaoEnfermagem
    """
    list_display = ['data']
    search_fields = ['data']

class SinalVitalAdmin(admin.ModelAdmin):
    """
    Admin para o model SinalVital
    """
    list_display = ['assinatura', 'hora']
    search_fields = ['assinatura', 'hora']



    # inlines = [Paciente]


admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Ala, AlaAdmin)
admin.site.register(Leito, LeitoAdmin)
admin.site.register(PrescricaoEnfermagem, PrescricaoEnfermagemAdmin)
admin.site.register(SinalVital, SinalVitalAdmin)
