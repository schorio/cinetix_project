from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    try:
        return arg - value
    except (TypeError, ValueError):
        return value
