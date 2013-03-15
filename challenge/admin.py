from django.contrib import admin
from challenge.models import Problem, Answer, User


class UserAdmin(admin.ModelAdmin):
	fields = ['username', 'points', 'grad_year']
	list_display = ('username', 'points', 'grad_year')
	search_fields = ['username', 'points', 'grad_year']

class ProblemAdmin(admin.ModelAdmin):
	fields = ['question', 'pub_date']
	list_display = ('question', 'pub_date')
	search_fields = ['question']
	date_hierarchy = 'pub_date'

class AnswerAdmin(admin.ModelAdmin):
	fields = ['answer', 'user', 'problem']
	list_display = ('answer', 'user', 'problem')
	search_fields = ['answer', 'user', 'problem'] 

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(User, UserAdmin)