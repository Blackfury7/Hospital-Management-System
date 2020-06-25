from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors,patients
from appointment . models import appointment_data
from django.db.models import Avg, Count, Min, Sum


#to show the basic details of the doctor (registration details)
def doctor_dashboard(request):
	
	if request.method=="POST":	


		data=json.loads(request.body)
		username=data['username']
		print(data)
		


		
		doctor_data=list(doctors.objects.filter(username=username).values())
		
		

		return JsonResponse(doctor_data,safe=False)


#Extra function --- No use of this function
def home(request):
	return HttpResponse("Wellcome to Django Home Page!!!")

#to show the list of doctors filtered
def doctor_list_by_department(request):
	
	if request.method=="POST":	


		data=json.loads(request.body)
		department=data['department']
		print(data)
		


		
		doctor_data=list(doctors.objects.filter(department=department).values('id','name','username'))
		# patient_data=list(appointment_data.objects.filter(doctor__department=department).values('doctor__name','patient__name'))

		
		

		return JsonResponse(doctor_data,safe=False)

def doctor_list(request):
	
	if request.method=="GET":	
		doctor_data=list(doctors.objects.all().values())
		return JsonResponse(doctor_data,safe=False)
def patient_list_under_doctor(request):
	if request.method == "POST":
		data=json.loads(request.body)
		id=data['id']
		# patient_list=list(patients.objects.filter(appointment_data__patient__id=id).filter(appointment_data__doctor_response="approved").order_by('appointment_data__date').values('id','name','wieght','height','appointment_data__status','appointment_data__date','appointment_data__time',appointment_data__id'))
		patient_list=list(patients.objects.filter(appointment_data__doctor_id=id).filter(appointment_data__doctor_response="approved").order_by('appointment_data__date').values())
		return JsonResponse(patient_list,safe=False)
