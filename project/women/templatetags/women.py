from django import template

from women.views import categories

register = template.Library()


@register.simple_tag
def get_categories():
    return categories


@register.inclusion_tag("women/categories.html")
def show_categories(selected_category=None):
    return {"selected_category": selected_category}
