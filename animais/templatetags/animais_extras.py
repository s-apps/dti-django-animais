import datetime
from django import template

register = template.Library()


@register.simple_tag
def data_acesso(format_string):
    return datetime.datetime.now().strftime(format_string)
