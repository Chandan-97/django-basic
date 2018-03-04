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
	random_numbers = []
	for i in range(random.randint(2, 8)):
		random_numbers.append(random.randint(0, 1000))
	return render(request, 'base.html', {"number":num,"num":even_or_odd, "random_numbers":random_numbers}) #response