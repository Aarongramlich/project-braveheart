from django.shortcuts import render
# from registration_app import urls
# from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,"registration_app/index.html"),

def stepOne(request):
	return render(request,"registration_app/stepone.html"),