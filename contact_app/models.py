from django.db import models

# Create your models here.

# class Prospect(models.Model):
# 	first_name = models.CharField()
# 	last_name = models.CharField()
# 	email = models.EmailField()

# 	def __str__(self):
# 		return self.first_name + self.last_name

class SupportRequest(models.Model):

	topic_choice = (
		('general question', 'General Question'),
		('data', 'Data'),
		('feedback','Issues/Feedback'),
		('technical question','Technical Question'),
		('product','Product Questions'),
		)

	topic = models.CharField(max_length=256,choices=topic_choice,default="--select--")
	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	# email = models.ForeignKey(Prospect, on_delete=models.SET_NULL,null=True)
	email = models.EmailField(max_length=256,blank=False)
	message = models.TextField(max_length=300,blank=False)

	def __str__(self):
		return self.topic + '-' + self.first_name + self.last_name

	def get_absolute_url(self):
		return ('submitted',[self.first_name])

