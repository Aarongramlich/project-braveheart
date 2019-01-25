from django.urls import path
from contact_app import views

app_name = 'contact_app'

urlpatterns = [
	path('',views.ContactUsCreateView.as_view(),name='contactus'),
	path('submitted/',views.SubmittedView.as_view(),name='submitted')

]