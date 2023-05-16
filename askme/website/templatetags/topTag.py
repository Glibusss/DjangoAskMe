from django import template
from ..models import Tag
from django.db.models import Count

register=template.Library()


@register.filter
def topTagAt(value):
    
    return Tag.objects.annotate(rat=Count('question')).order_by('-rat')[value].tag or ""