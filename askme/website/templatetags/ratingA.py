from django import template
from ..models import answerVote


register=template.Library()


@register.filter
def ratingA(value):
    likes = answerVote.objects.all().filter(score=1,answer__id=value.id).count()
    dises = answerVote.objects.all().filter(score=-1,answer__id=value.id).count()
    return likes-dises