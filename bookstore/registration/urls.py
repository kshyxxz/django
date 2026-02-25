from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
	path('form/',views.registration_form, name='form'),
	path('form/sql/',views.registration_form_sql_injection, name='form_sql'),
	path('',views.list_user, name='list'),
]
