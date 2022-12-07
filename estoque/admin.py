from django.contrib import admin
from estoque.models import produto


class DisplayAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'codigo', 'descricao',
                    'quantidade', 'undMedida', 'categoria']


admin.site.register(produto, DisplayAdmin)
