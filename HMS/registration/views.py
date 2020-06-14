from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors, patients


def doctor_registration(request):
	
	if request.method=="POST":	


		data=json.load(request)
		
		
		try:


				
			doctors.objects.create(**data)
			message="success"

		except:
			message="error"

		
		

		return JsonResponse(message,safe=False)

def patient_registration(request):
	
	if request.method=="POST":	


		data=json.load(request)
		
		
		try:

			patients.objects.create(**data)
			
			message="success"

		except:
			message="error"

		
	
		
		

		return JsonResponse(message,safe=False)
