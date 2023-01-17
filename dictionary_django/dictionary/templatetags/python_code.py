from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@stringfilter
@register.tag(name='stripWord')
def stripWord(value, arg):
    arg=' '
    return value.replace(arg, '')

