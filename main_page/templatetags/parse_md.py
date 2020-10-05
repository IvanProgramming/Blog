from django import template
import mistune

register = template.Library()


@register.filter
def md2html(arg):
    return mistune.html(arg)
