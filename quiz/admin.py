from django.contrib import admin
from .models import Category,Quiz ,Question ,Answer
# from .models import *
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

class AnswersInline(SuperInlineModelAdmin, admin.TabularInline):
    model = Answer
    extra = 4


class QuestionInline(SuperInlineModelAdmin, admin.StackedInline):
    model = Question
    extra = 1
    inlines = [AnswersInline]


class QuizAdmin(SuperModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answerText', 'isRight')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'title', 'difficulty')
    inlines = [AnswersInline]
 


admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)



