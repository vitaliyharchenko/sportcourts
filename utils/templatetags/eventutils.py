# coding=utf-8
__author__ = 'vitaliyharchenko'

from django import template
from events.models import Event

register = template.Library()

@register.inclusion_tag('tagtemplates/event.html')
def event_pane(event):
    context = {'event': event.as_leaf_class}
    # if event.content_type.model == 'game':
    #     context['sub_count'] = event.subscribed.count()
    return context