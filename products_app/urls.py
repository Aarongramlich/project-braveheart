from django.urls import path
from products_app import views

app_name = 'products_app'

urlpatterns = [
	path('packages/',views.ProductPackageView.as_view(),name='packages'),
]