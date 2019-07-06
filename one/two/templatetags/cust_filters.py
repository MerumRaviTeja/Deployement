from django import template
register=template.Library()
@register.filter(name='c_and_c')
def first_eight_upper(value,arg):
    result=value[:8].upper()+str(arg)
    return result