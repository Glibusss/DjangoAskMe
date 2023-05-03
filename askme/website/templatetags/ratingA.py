from django import template
from ..models import AnswerVote


register=template.Library()


@register.filter
def ratingA(value):
    likes = AnswerVote.objects.all().filter(score=1,answer__id=value.id).count()
    dises = AnswerVote.objects.all().filter(score=-1,answer__id=value.id).count()
    return likes-dises