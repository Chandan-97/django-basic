from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.
# Class based views

class HomeView(TemplateView):
	template_name = "home.html"
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		num = random.randint(0, 100000)
		even_or_odd = "none"
		if(num%2==0):
			even_or_odd = "even"
		else:
			even_or_odd = "odd"
		random_numbers = []
		for i in range(random.randint(2, 8)):
			random_numbers.append(random.randint(0, 1000))
		context = {
			"number"		: num,
			"num"			: even_or_odd, 
			"random_numbers":random_numbers,
		}
		return context

class AboutView(TemplateView):
	template_name = "about.html"

class ContactView(TemplateView):
	template_name = "contact.html"