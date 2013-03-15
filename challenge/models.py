from django.db import models

# Create your models here.

class User(models.Model):
	username 	= models.CharField(max_length=16)
	grad_year 	= models.DateField('grad year')
	points 		= models.IntegerField(default=0)
	def __unicode__(self):
		return self.username

class Problem(models.Model):
    question 	= models.CharField(max_length=1024)
    pub_date 	= models.DateTimeField('date published')
    def __unicode__(self):
    	return self.question

class Answer(models.Model):
    problem 	= models.ForeignKey(Problem)
    answer 		= models.CharField(max_length=200)
    user 		= models.ForeignKey(User)
    def __unicode__(self):
    	return self.answer