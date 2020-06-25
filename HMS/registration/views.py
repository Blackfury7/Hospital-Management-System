from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import doctors, patients

#to register the doctor account
def doctor_registration(request):
	
	if request.method=="POST":	


		data=json.loads(request.body)
		username=data['username']
		email=data['email']
		print(data)

		try:


			if doctors.objects.filter(username=username).exists():
			    message='Username is taken'
			elif doctors.objects.filter(email=email).exists():
			    message='Email is taken'
			else:
				doctors.objects.create(**data)
				message="success"

		except:
			message="error"

		
		

		return JsonResponse(message,safe=False)
#to register the patient
def patient_registration(request):
	
	if request.method=="POST":	


		data=json.loads(request.body)
		print(data)
		username=data['username']
		

		
		
		try:
			print("user enter")
			
			if patients.objects.filter(username=username).exists():
			    print("username")
			    message='This username is already taken'
			else:
				print("before data entry")
				patients.objects.create(**data)
				print("data entry")

				message="success"

		except:
			print("error")
			message="error"
		finally:
			print("The 'try except' is finished")

		
	
		
		

		return JsonResponse(message,safe=False)


def check_username_already_exists(request):
	
	if request.method=="POST":	


		data=json.loads(request.body)
		print(data)
		username=data['username']
		try:
			
			
			if patients.objects.filter(username=username).exists():
			    print("username")
			    message='This username is already taken'
			elif doctors.objects.filter(username=username).exists():
			    print("username alredy taken")
			    message='This username is already taken'
			else:
			
				print("unique username")

				message="unique"

		except:
			print("error")
			message="error"
		finally:
			print("The 'try except' is finished")

		
	
		
		

		return JsonResponse(message,safe=False)

