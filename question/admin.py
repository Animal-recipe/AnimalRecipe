from django.contrib import admin
from .models import Answer, Question
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['id', 'is_active', 'title']
    list_display_links = ['id', 'title']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
