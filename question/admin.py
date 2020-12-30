from django.contrib import admin
from .models import Answer, Question
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['id', 'is_active', 'title']
    list_display_links = ['id', 'title']
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['id', 'is_active', 'question', 'content']
    list_display_links = ['id', 'content']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
