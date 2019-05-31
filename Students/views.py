from django.shortcuts import render

from .models import Students


def is_valid_queryparam(param):
	return param != '' and param is not None


def index(request):
	data = Students.objects.all()

	insuranceNumber = request.GET.get('insuranceNumber')
	lastName = request.GET.get('lastName')
	yearOfBirth = request.GET.get('yearOfBirth')
	cityOfBirth = request.GET.get('cityOfBirth')

	if is_valid_queryparam(insuranceNumber):
		data = data.filter(insuranceNumber__contains = insuranceNumber)
	if is_valid_queryparam(lastName):
		data = data.filter(lastName__icontains = lastName)
	if is_valid_queryparam(yearOfBirth):
		data = data.filter(yearOfBirth__contains = yearOfBirth)
	if is_valid_queryparam(cityOfBirth):
		data = data.filter(cityOfBirth__icontains = cityOfBirth)

	context = {
		'data': data
	}

	return render(request, 'Students/index.html', context)