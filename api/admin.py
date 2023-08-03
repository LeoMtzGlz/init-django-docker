from django.contrib import admin
from .models import Task, Comment
# api.models es lo mismo que .models


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
