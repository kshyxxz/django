from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
	path('form/',views.registration_form, name='form'),
	path('',views.list_user, name='list'),
]
