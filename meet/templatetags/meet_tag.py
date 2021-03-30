from django import template

register = template.Library()


@register.simple_tag
def number_list(value):
    value += 1

    return value