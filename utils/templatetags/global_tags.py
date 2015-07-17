from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
import re

register = template.Library()


@register.inclusion_tag('tagtemplates/avatar.html')
def avatar(avatar_field, size='30', circle=False, sex='m', thumbnail='False'):
    size = str(size)
    return {'avatar_field': avatar_field, 'circle': circle, 'size': size + 'x' + size, 'side_size': size, 'sex': sex, 'thumbnail': thumbnail}


@register.simple_tag(takes_context=True)
def active(context, urlname):
    try:
        pattern = '^' + reverse(urlname)
    except NoReverseMatch:
        pattern = urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''