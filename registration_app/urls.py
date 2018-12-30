from django.urls import path
from registration_app import views

urlpatterns = [
	path('',views.index,name="index"),
	path('stepOne/',views.stepOne,name="stepOne"),
]