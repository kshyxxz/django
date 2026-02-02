from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse

monthly_challenges = {
    'january': 'Exercise daily for 30 minutes',
    'february': 'Read one book',
    'march': 'Learn something new each day',
    'april': 'Drink at least 2 liters of water daily',
    'may': 'Wake up early every day',
    'june': 'Practice a new skill for 20 minutes daily',
    'july': 'Avoid junk food for the entire month',
    'august': 'Write a daily journal entry',
    'september': 'Learn and revise one topic each day',
    'october': 'Limit social media usage to 30 minutes per day',
    'november': 'Express gratitude by writing one thankful note daily',
    'december': None,
}

def index(request):
	list_items = ""
	months = list(monthly_challenges.keys())
	return render(request, 'pilot/index.html', { 'months':months})

def monthly_challenge(request, month):
	try:
		challenge_text = monthly_challenges[month.lower()]
		return render(request, 'pilot/challenge.html', {'text' : challenge_text, 'month_name' : month})
	except:
				raise Http404()
	
def monthly_challenge_by_number(request,month):
	months = list(monthly_challenges.keys())
	redirect_month = months[month-1]
	redirect_url = reverse("monthly-challenge", args=[redirect_month])
	return redirect(redirect_url)