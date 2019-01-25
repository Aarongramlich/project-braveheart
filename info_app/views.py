from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class WhatView(TemplateView):
	template_name = 'info_app/what.html'

class HowView(TemplateView):
	template_name = 'info_app/how.html'

class IndexView(TemplateView):
	template_name = 'index.html'
