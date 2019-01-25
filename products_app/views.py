from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,CreateView

# Create your views here.

class IndexView(TemplateView):
	template_name = 'index.html'

class ProductPackageView(TemplateView):
	template_name = 'products_app/product_packages.html'