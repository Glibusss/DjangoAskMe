from django.contrib import admin


from . import models
# Register your models here.

admin.site.register(models.question)

admin.site.register(models.answer)

admin.site.register(models.tag)


admin.site.register(models.user)