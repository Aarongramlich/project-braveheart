from registration_app.models import Member
from django import forms

class RegStepOneForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('first_name','last_name','email','birthdate')
