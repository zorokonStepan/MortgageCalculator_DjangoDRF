from django import template
register = template.Library()


@register.filter
def index(indexable, i):
    """to output sequence elements by indexes in an html template
    param: indexable - sequence
    param: i - index
    """
    return indexable[i]
