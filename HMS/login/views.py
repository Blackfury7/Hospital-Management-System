from django.shortcuts import render


from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors, patients



def login(request):
	if request.method=="POST":
		data=json.loads(request.body)
		print(data)
		username=data['username']
		password=data['password']


		
		doctor=doctors.objects.filter(username=username, password= password)
		patient=patients.objects.filter(username=username, password= password)
		if username=="receptionist" and password=="1234":
			message="receptionist"
			
		elif doctor.exists():
			message="doctor"
		elif patient.exists():
			message="patient"
		else:
			message="invalid details"

	return JsonResponse(message,safe=False)

