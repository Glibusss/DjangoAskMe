from django import template
from ..models import tag
from django.db.models import Count

register=template.Library()


@register.filter
def topTagAt(value):
    
    return tag.objects.annotate(rat=Count('question')).order_by('-rat')[value].tag