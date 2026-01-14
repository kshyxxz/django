from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Welcome')

def january(request):
	return HttpResponse('Janyary plans : Exercise')

def february(request):
	return HttpResponse('February plabs : Eat Healthy')

def march(request):
	return HttpResponse('March plans : Workout Daily')