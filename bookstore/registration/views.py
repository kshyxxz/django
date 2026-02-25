from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

def list_user(request):
	users = Registration.objects.all()
	user_input = "this is user inptut"
	return render(request, 'registration/list.html', {'users': users, 'user_input': user_input})

@csrf_exempt
def registration_form_sql_injection(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data
			hashPass = make_password(data['password'])
			
			sql = f"INSERT INTO registration_registration (name, email, password) VALUES ('{data['name']}', '{data['email']}', '{hashPass}')"
			with connection.cursor() as cursor:
				cursor.execute(sql)
			print("Success")

			return render(request, 'registration/form.html', {
				'form': RegistrationForm(),
				'success': "Successful"
			})
		
	else:
		form = RegistrationForm()

	return render(request, 'registration/form.html', {'form': form})

def registration_form(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data
			hashPass = make_password(data['password'])
			registration = Registration(name=data['name'],email=data['email'],password=hashPass)
			registration.save()
			print("Success")
			return render(request, 'registration/form.html', {
				'form': RegistrationForm(),
				'success': "Successful"
			})
		
	else:
		form = RegistrationForm()

	return render(request, 'registration/form.html', {'form': form})