from django import template


register = template.Library()


@register.inclusion_tag('tagtemplates/avatar.html')
def avatar(avatar_field, size='30', circle=False):
    size = str(size)
    return {'avatar_field': avatar_field, 'circle': circle, 'size': size + 'x' + size, 'side_size': size}