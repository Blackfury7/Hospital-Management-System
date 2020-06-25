from django.shortcuts import render


from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from registration . models import doctors, patients
from appointment . models import appointment_data

#function to create medical report of the patient'appointment by the doctor
def add_medical_report(request):
	if request.method == "POST":
		data=json.loads(request.body)
		appointment_id=data['id']
		print(data)
	
		appointment_data.objects.filter(id=appointment_id).update(status="Done",**data)
		message='medical report generated'

		


		return JsonResponse(message,safe=False)







