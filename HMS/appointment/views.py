from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors, patients
from . models import appointment_data

#to create new appointment by the patient
def patient_appointment(request):

	if request.method =="POST":
		data=json.loads(request.body)
		print(data)

		try:
			appointment_data.objects.create(patient_id=data['patient_id'] ,doctor_id=data['doctor_id'], problem=data['problem'],payment_status=data['payment_status'],date=data['date'],time=data['time'])
			print('success')
			message="Appointment is registered. You will be notified soon."
		except:
			message="Error"

	return JsonResponse(message,safe=False)


#to show all the new appointment request to receptionist
def receptionist_appointment_requests(request):
	if request.method == "GET":




		appt_request=list(appointment_data.objects.filter(receptionist_response="pending").order_by('date').values('id','doctor__name','patient__name','status','payment_status','date','time','time_of_registering_appointment','receptionist_response','receptionist_reason','doctor_response'))

		return JsonResponse(appt_request,safe=False)



#to show the status of appointment to the patient
 # BUT THIS FUNCTION IS ALSO MADE IN PATIENT APP
# def patient_appointment_details(request):
# 	if request.method == "POST":
# 		data=json.loads(request.body)
# 		print(data)
# 		id=data['id']




# 		appt_request=list(appointment_data.objects.filter(id=id).order_by('date').values('id','doctor__name','patient__name','status','doctor_id','doctor__department','patient_id','patient__phone_no','problem','payment_status','before_disease','after_disease','date','time','time_of_registering_appointment','prescription','receptionist_response','receptionist_reason','doctor_response'))

# 		return JsonResponse(appt_request,safe=False)
	#


	#to update the response given by the receptionist and the doctor
def updating_response_of_appointment(request):
	if request.method == "POST":
		data=json.loads(request.body)
		appointment_id=data['id']
		print(data)
		
		try:
			appointment_data.objects.filter(id=appointment_id).update(**data)
			message="Your response is recieved"
		except:
			message="error"

		return JsonResponse(message,safe=False)

#to show the current/live appointments list of a specific doctor 
#these appointments are approved by the docter and they are going to happen in future
def doctor_live_appointments_list(request):
	if request.method == "POST":
		data=json.loads(request.body)
		doctor_id=data['id']





		appt_request=list(appointment_data.objects.filter(doctor_id=doctor_id).filter(doctor_response="approved").filter(status="Active").order_by('date').values('id','patient__name','problem','date','time'))

		return JsonResponse(appt_request,safe=False)

#to show the current/live appointment details of a patient under a specific doctor 
#this appointment is approved by the docter and it is going to happen in future
def doctor_live_appointment_details(request):
	if request.method == "POST":
		data=json.loads(request.body)
		appointment_id=data['id']





		appt_request=list(appointment_data.objects.filter(id=appointment_id).filter(doctor_response="approved").filter(status="Active").order_by('date').values('id','doctor__name','patient_id','patient__name','status','patient__gender','patient__dob','patient__email','patient__address','problem','patient__height','patient__weight','patient__blood','before_disease','after_disease','date','time',))

		return JsonResponse(appt_request,safe=False)







#to show the appointment requests passed by RECEPTIONIST to doctor
def doctor_appointment_requests(request):
	if request.method == "POST":
		data=json.loads(request.body)
		pk=data['id']





		appt_request=list(appointment_data.objects.filter(doctor_id=pk).filter(doctor_response="pending").filter(receptionist_response="approved").order_by('date').values('id','doctor__name','patient__name','status','payment_status','date','time','time_of_registering_appointment','receptionist_response','receptionist_reason','doctor_response'))

		return JsonResponse(appt_request,safe=False)

#to show status/response of appointment request to doctor of specific patient with specific appointment id 
#THis is used when doctor sees appointment request in detail ( in view details function at frontend) 
def show_appointment_request_details(request):
	
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		patient_data=list(appointment_data.objects.filter(id=id).order_by("date").values('id','status','patient__name','doctor_response','doctor_reason','doctor__name','problem','date','time','before_disease','is_modify_by_doc'))


		return JsonResponse(patient_data,safe=False)
 