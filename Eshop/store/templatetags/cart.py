from django import template

register = template.Library()

@register.filter(name='to_int')
def to_int(value):
    return int(value)

@register.filter(name='total_price')
def total_price(vaue,price):
    return vaue*price