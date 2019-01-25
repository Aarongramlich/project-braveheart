from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from contact_app.forms import ServiceRequestForm
from django.views.generic.edit import FormView
from django import forms
from . import models
from django.urls import reverse, reverse_lazy

# Create your views here.

# class ContactUsView(TemplateView):
# 	template_name = 'contact_app/contact_us.html'

class ContactUsCreateView(CreateView):
	fields = ('topic','first_name','last_name','email','message')
	model = models.SupportRequest
	template_name = 'contact_app/contact_us.html'
	# success_url = reverse_lazy("contact_app: submitted")


# def RequestCreateView(request):
# 		if request.method == 'POST':
# 			form = ServiceRequestForm(request.POST)
# 			if form.is_valid():
# 				redirect('home')
# 		else:
# 		  form = ServiceRequestForm()
# 		  return render(request, 'contact_app/contact_us.html', {'form': form})

class SubmittedView(TemplateView):
	template_name = 'contact_app/submitted_contact_us.html'