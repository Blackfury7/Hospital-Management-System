from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import patients,doctors
from appointment . models import appointment_data
from django.db.models import Q

#to show the basic details of patient which were recorded at the time of registration
def patient_basic_details(request):
	data=json.loads(request.body)
	username=data['username']
	print(data)
	patient_data=list(patients.objects.filter(username=username).values())
	return JsonResponse(patient_data,safe=False)

#to show medical history of patient .medical history contains the details of all appointments done by the patient.
def show_medical_history(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)

		patient_data=list(appointment_data.objects.filter(patient_id=id).filter(status="Done").order_by("-date").values('id','patient__name','doctor__name','doctor_id','problem','report','prescription','date','time','before_disease','after_disease'))


		return JsonResponse(patient_data,safe=False)


#function to show show current/live appointments of patient which are approved by the doctor and which are going to take place in future 
def show_current_appointments(request):
	
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		patient_data=list(appointment_data.objects.filter(patient_id=id).filter(status="Active").order_by("date").values('id','patient__name','receptionist_response','receptionist_reason','doctor_response','status','doctor_reason','doctor__name','doctor_id','problem','report','prescription','date','time','before_disease','after_disease','is_modify_by_doc'))


		return JsonResponse(patient_data,safe=False)


#to show status/response of appointment request to patient
def appointment_request(request):
	
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		patient_data=list(appointment_data.objects.filter(patient_id=id).filter(Q(status="pending")|Q(status='rejected')|Q(status='Active')).order_by("date").values('id','status','patient__name','receptionist_response','receptionist_reason','doctor_response','doctor_reason','doctor__name','doctor_id','problem','date','time','before_disease','is_modify_by_doc'))


		return JsonResponse(patient_data,safe=False)

#to show the prescription given by the doctor of the recent appointment		
def show_current_prescription(request):
	
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		patient_data=list(appointment_data.objects.filter(patient_id=id).filter(status="Done").order_by('-date').values('id','patient__name','doctor__name','doctor__id','prescription','date','time','after_disease'))


		return JsonResponse(patient_data,safe=False)
		
#to show payment history of the all the appointments requested by the patient (sin)
def show_payment_history(request):

	
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		patient_data=list(appointment_data.objects.filter(patient_id=id).filter(doctor_response="Approved").order_by("-time_of_registering_appointment").values('patient__name','doctor__name','doctor_id','after_disease','amount','date','time','time_of_registering_appointment'))


		return JsonResponse(patient_data,safe=False)




#To show list of patients on receptionist dashboard who has DONE atleast one appointment OR DOING his/her 1st appointment with ANY DOCTOR
def patient_list_appointment(request):
	
	if request.method=="GET":	
		patient=list(patients.objects.filter(appointment_data__doctor_response="Approved").values())
		return JsonResponse(patient,safe=False)

#This fuction is to send list of all registered patients to receptionist
def patient_list(request):
	
	if request.method=="GET":	
		patient=list(patients.objects.all().values())
		return JsonResponse(patient,safe=False)

#To show list of patients on receptionist dashboard who had atleast one appointment with a PARTICULAR/SPECIFIC doctor
#THIS FUNCTION IS ALSO IN DOCTOR APP
# def patient_list_under_doctor(request):
# 	if request.method == "POST":
# 		data=json.loads(request.body)
# 		id=data['id']
# 		appt_request=list(appointment_data.objects.filter(doctor_id=id).annotate("patient_id",unique=True).order_by('date').values('id','doctor__name','patient__name','status','payment_status','date','time','time_of_registering_appointment','receptionist_response','receptionist_reason','doctor_response'))

# 		return JsonResponse(appt_request,safe=False)


