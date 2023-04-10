from django import template
from ..models import questionVote

register=template.Library()


@register.filter
def ratingQ(value):
    likes = questionVote.objects.all().filter(score=1,question__id=value.id).count()
    dises = questionVote.objects.all().filter(score=-1,question__id=value.id).count()
    return likes-dises