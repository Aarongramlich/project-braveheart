from django.urls import path
from info_app import views

app_name = 'info_app'

urlpatterns = [
	path('what/',views.WhatView.as_view(),name='what'),
	path('how/',views.HowView.as_view(),name='how'),
]