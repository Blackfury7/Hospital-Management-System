from django.shortcuts import render


from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors, patients



def login(request):
	if request.method=="POST":
		data=json.load(request)
		username=data['username']
		passwrd=data['password']


		
		doctor=doctors.objects.filter(username=username, password= password)
		patient=patients.objects.filter(username=username, password= password)
		if username=="receptionist" and password=="1234":
			message="receptionist"
		elif not doctor:
			message="doctor"
		elif not patient:
			message="patient"
		else:
			message="invalid details"

	return JsonResponse(message,safe=False)

