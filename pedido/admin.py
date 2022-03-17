from django.contrib import admin
from pedido.models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ] 



admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)
