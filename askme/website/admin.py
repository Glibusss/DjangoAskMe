from django.contrib import admin


from . import models


admin.site.register(models.question)


admin.site.register(models.answer)


admin.site.register(models.tag)


admin.site.register(models.Profile)


admin.site.register(models.questionVote)


admin.site.register(models.answerVote)

