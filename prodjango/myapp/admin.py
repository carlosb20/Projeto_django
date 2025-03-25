from django.contrib import admin
from .models import Orcamento

class adminOrcamento(admin.ModelAdmin):
    list_display = ('peca','preco')


admin.site.register(Orcamento,adminOrcamento)
