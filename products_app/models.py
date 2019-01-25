from django.db import models

# Create your models here.


class ProductPackage(models.Model):

	package_name = models.CharField(max_length=256)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField(max_length=2000)

	def __str__(self):
		return self.package_name

class Companies(models.Model):

	request_method_choice = (
		('email','Email'),
		('api','API'),
		('phone','Phone'),
		('mail','Physical Mail'),
		('webform','Webform'),
		('portal','Portal'),
		)

	industry_choice = (
		('aerospace','Aerospace'),
		('agriculture','Agriculture'),
		('pharmaceutical','Pharmaceutical'),
		('software','Software'),
		('hardware','Hardware'),
		('construction','Construction'),
		('defense','Defense'),
		('education','Education'),
		('energy','Energy'),
		('entertainment','Entertainment'),
		('financial_services','Financial Services'),
		('food','Food'),
		('healthcare','Healthcare'),
		('hospitality','Hospitality'),
		('information','Information'),
		('manufacturing','Manufacturing'),
		('automotive','Automotive'),
		('broadcasting','Broadcasting'),
		('film','Film'),
		('music','Music'),
		('news','News'),
		('publishing','Publishing'),
		('internet','Internet'),
		('transportation','Transporation'),
		('services','Services'),
		)

	company_name = models.CharField(max_length=256)
	packages = models.ManyToManyField(ProductPackage)
	website = models.URLField(max_length=2000,null=True)
	primary_request_method = models.CharField(max_length=256,choices=request_method_choice,null=True)
	secondary_request_method = models.CharField(max_length=256,choices=request_method_choice,null=True)
	industry = models.CharField(max_length=256,choices=industry_choice,null=True)


	def __str__(self):
		return self.company_name
