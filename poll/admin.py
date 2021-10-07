from django.contrib import admin
from .models import Question, Answer, Choice, IdIp


class QuestionAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'pub_date',
		'end_date',
		'active',
	)


class ChoiceAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'question',
		'lock_other',
	)
	list_filter = ('question',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)


