from cpe400.models import Problem, Answer
from django.contrib import admin

class ProblemAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields' : ['question']}),
		('Date information',{'fields' : ['pub_date']}),
	]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['pub_date']
	date_hierarchy = 'pub_date'


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Answer)