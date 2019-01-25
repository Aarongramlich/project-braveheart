from registration_app.models import Member
from crispy_forms.helper import FormHelper
from django import forms
from . import models

class ServiceRequestForm(forms.ModelForm):
	class Meta:
		model = models.SupportRequest
		fields = ('first_name','last_name','email','message')
