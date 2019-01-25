from django.urls import path
from registration_app import views


app_name = 'registration_app'

urlpatterns = [
	# path('stepone/',views.StepOneCreateView.as_view(),name="stepone"),
	path('stepone/',views.StepOneCreateView.as_view(),name="stepone"),
	path('steptwo/',views.StepTwoCreateView.as_view(),name="steptwo"),
]