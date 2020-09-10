from django import template

register = template.Library()


@register.filter(name='category')
def category(cate,product_cate):
    print(cate)
    print(product_cate)
    if str(cate) == str(product_cate):
        return True
    
@register.filter(name='categorys')
def categorys(subcate,cate):
    if subcate == cate:
        return True