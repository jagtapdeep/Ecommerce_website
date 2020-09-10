from django import template

register = template.Library()


@register.filter(name='condition')
def condition(customer_name,user_name):
    if customer_name == user_name:
        return True