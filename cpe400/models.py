from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Problem(models.Model):
	question = models.CharField(max_length=1024)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(minutes=5)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = "True"
	was_published_recently.short_description = 'Published recently?'

class Answer(models.Model):
	problem = models.ForeignKey(Problem)
	answer = models.CharField(max_length=1024) 
	user = models.CharField(max_length=16)
	def __unicode__(self):
		return self.user + ": " + self.answer