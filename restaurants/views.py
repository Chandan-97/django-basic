from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
# function based views
def home(request):
	# return HttpResponse("Hello")
	num = random.randint(0, 100000)
	even_or_odd = "none"
	if(num%2==0):
		even_or_odd = "even"
	else:
		even_or_odd = "odd"
	return render(request, 'base.html', {"number":num,"num":even_or_odd}) #response