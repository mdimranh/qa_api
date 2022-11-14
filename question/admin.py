from django.contrib import admin

from .models import Answer, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'total_answer']

admin.site.register(Answer)