from django import template

register = template.Library()

@register.filter(name='get_related')
def get_related(obj):
    if len(obj.all()) == 0:
        return ""
    return obj.all()[0].book_title
