from django.db import models
from phone_field import PhoneField
from datetime import date
from products_app.models import ProductPackage

# Create your models here.

class Member(models.Model):

	communication_preference_options = (
		('email','Email'),
		('phone','Phone'),
		('text','Text'),
		)

	first_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length=256)
	email = models.EmailField(max_length=256,unique=True)
	phone = PhoneField(blank=True,E164_only=False)
	communication_preference = models.CharField(max_length=256,choices=communication_preference_options)
	opt_out = models.BooleanField(blank=True)
	hard_bounce = models.BooleanField(blank=True)
	employer = models.CharField(max_length=256,blank=True)
	ssn = models.CharField(max_length=11,blank=True)
	drivers_license_number = models.CharField(max_length=8,blank=True)
	birthdate = models.DateField(blank=True)
	created_date = models.DateField(auto_now_add=True,editable=False)
	last_updated = models.DateField(auto_now=True,editable=False)
	package = models.ForeignKey(ProductPackage,on_delete=models.SET_NULL,blank=True,null=True)
	# service_requests = models.ManyToManyField()
