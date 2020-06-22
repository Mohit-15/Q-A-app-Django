from django.contrib import admin
from .models import Question , Answer

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
	model = Answer
	list_filter = ('ans_title',)

class QuestionAdmin(admin.ModelAdmin):
	model = Question
	list_filter = ('ques_title',)

admin.site.register(Question, QuestionAdmin)          # registering the models 
admin.site.register(Answer, AnswerAdmin)

