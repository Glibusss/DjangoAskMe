from django import template
from ..models import QuestionVote

register=template.Library()


@register.filter
def ratingQ(value):
    likes = QuestionVote.objects.all().filter(score=1,question__id=value.id).count()
    dises = QuestionVote.objects.all().filter(score=-1,question__id=value.id).count()
    return likes-dises