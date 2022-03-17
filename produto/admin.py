from django.contrib import admin
from produto.models import Produto, Variacao



class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','get_preco_formatado','get_preco_formatado_desconto']
    inlines = [
        VariacaoInline
    ]
    


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)

