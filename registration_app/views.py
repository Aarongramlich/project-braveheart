from django.shortcuts import render
from . import models
from registration_app.forms import RegStepOneForm
from django.views.generic.edit import FormView
from django import forms
from django.views.generic import (View, TemplateView, ListView, DetailView, 
										 CreateView,DeleteView,UpdateView)
from django.urls import reverse, reverse_lazy


# Create your views here.

class IndexView(TemplateView):
	template_name = 'index.html'

# def index(request):
# 	return render(request,"index.html"),

# class StepOneView(TemplateView):
# 	model = models.Member
# 	template_name = "registration_app/step_one.html"

class StepOneCreateView(CreateView):
	fields = ('first_name','last_name','email','birthdate')
	model = models.Member
	# form_class = RegStepOneForm
	template_name = "registration_app/step_one.html"
	success_url = reverse_lazy('registration_app: steptwo')

# USE THE FOLLOWING FUNCTION IF YOU NEED TO USE A FORM FOR STEP ONE CREATE VIEW
 	# def StepOneCreateView(request):
	# 	if request.method == 'POST':
	# 		form = RegStepOneForm(request.POST)
	# 		if form.is_valid():
	# 			redirect('home')
	# 	else:
	# 	  form = RegStepOneForm()
	# 	  return render(request, 'registration_app/step_one.html', {'form': form})

class StepTwoCreateView(CreateView):
	fields = ('test_field',)
	model = models.Member
	template_name = "registration_app/step_two.html"