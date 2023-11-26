import datetime
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return '#'


@register.simple_tag()
def mediapath(val):
    return f'/media/{val}'


@register.simple_tag()
def moder_groups():
    return Group.objects.get(name='moderator')


@register.simple_tag()
def user_groups():
    return Group.objects.get(name='user')
