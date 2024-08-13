from django.contrib import admin

# Register your models here.
from .models import Visitante

@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo', 'cpf', 'data_nascimento', 'numero_casa', 
        'placa_veiculo', 'hora_chegada', 'hora_saida', 
        'hora_autorizacao', 'nome_morador', 'porteiro_autorizou'
    ]
    search_fields = ['nome_completo', 'cpf']
    list_filter = ['data_nascimento', 'hora_chegada']
