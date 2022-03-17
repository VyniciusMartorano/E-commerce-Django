from django import template
from utils.price_format import format_value
from utils import utils

register = template.Library()



@register.filter(name='price_filter')
def price_filter(txt):
    formatado = format_value(txt)
    return formatado


@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)

@register.filter
def cart_totals(carrinho):
    return utils.cart_total(carrinho)

