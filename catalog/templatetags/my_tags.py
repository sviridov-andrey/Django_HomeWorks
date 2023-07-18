import datetime
from django import template

register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return '#'


@register.simple_tag
def mediapath(val):
    return f'/media/{val}'
