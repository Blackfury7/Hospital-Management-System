from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors, patients


def doctor(request):
	
	if request.method=="POST":	


		data=json.load(request)
		uername=data['username']
		


		
		doctor=list(doctors.objects.filter(username=username))
		
		

		return JsonResponse(doctor,safe=False)

