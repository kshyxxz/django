from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.hashers import make_password

def list_user(request):
	users = Registration.objects.all()
	user_input = "this is user inptut"
	return render(request, 'registration/list.html', {'users': users, 'user_input': user_input})

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