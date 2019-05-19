from django.contrib import admin
from uttar.models import Topic, Question, Answer, Like

admin.site.register(Topic)
admin.site.register(Like)

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["topic", "status", "ask_date"]
    list_display = ["question", "topic", "status"]
    search_fields = ["question", "topic"]
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_filter = ["ans_by", "question"]
    list_display = ["question", "answer"]
    search_fields = ["question", "answer"]
admin.site.register(Answer, AnswerAdmin)
