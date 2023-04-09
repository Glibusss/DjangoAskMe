from django.contrib import admin


from . import models


admin.site.register(models.question)


admin.site.register(models.answer)


admin.site.register(models.tag)


admin.site.register(models.user)


admin.site.register(models.upvoteQuestion)


admin.site.register(models.downvoteQuestion)


admin.site.register(models.upvoteAnswer)


admin.site.register(models.downvoteAnswer)