from django import template
from rango_app.models import Category

register = template.Library()


@register.inclusion_tag('categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all()}
