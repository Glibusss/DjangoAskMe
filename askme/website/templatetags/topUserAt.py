from django import template
from ..models import user
from django.db.models import Count,F

register=template.Library()


@register.filter
def topUserAt(value):
    
    return user.objects.annotate(questions=Count('question',distinct=True),answers=Count('answer',distinct=True)).annotate(
        rat=F('questions')+F('answers')).order_by('-rat')[value].username