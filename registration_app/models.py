from django.db import models

# Create your models here.

class Member(models.Model):
	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	email = models.EmailField(max_length=256,blank=False)
	birthdate = models.DateField(blank=False)
	registration_date = models.DateTimeField(blank=True,auto_now_add=True)

	def __str__(self):
		return self.first_name + self.last_name


