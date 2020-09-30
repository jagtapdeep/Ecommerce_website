from django import template

register = template.Library()


@register.filter(name='review')
def review(product_id,feedback_id):
    if product_id == feedback_id:
        return True

@register.filter(name='available')
def available(product_quantity):
    if product_quantity != 0:
        return True



@register.filter(name='availables')
def availables(product_quantity):
    if product_quantity <= 10:
        return True


@register.filter(name='offer')
def offer(product_offer):
    if product_offer == 0:
        return True

@register.filter(name='offer_price')
def offer_price(product_price,product_offer):
    if product_offer != 0:
        a = product_price * product_offer
        b = a/100
        c = product_price - b
        return int(c)
    else:
        return product_price

@register.filter(name='length')
def length(list_len):
    if len(list_len) == 0:
        return False
    else:
        return True

@register.filter(name='offer_total_price')
def offer_total_price(product_price,product_quantity):
    return product_price * product_quantity


@register.filter(name='product_price')
def product_price(product_price,product_quantity):
    return ( product_price / product_quantity )