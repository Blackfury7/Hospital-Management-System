from django.db import models
from registration . models import doctors, patients

# Create your models here.

class appointment_data(models.Model):

	patient=models.ForeignKey(patients , on_delete = models.CASCADE)
	doctor=models.ForeignKey(doctors , on_delete = models.CASCADE)

	problem= models.CharField(max_length = 1000)
	payment_status= models.CharField(max_length = 200, default="Pending")
	amount= models.CharField(max_length = 200, default="500")

	before_disease= models.CharField(max_length = 200, blank=True)
	after_disease= models.CharField(max_length = 200, blank=True)

	
	report= models.CharField(max_length = 200, blank=True)
	date= models.CharField(max_length = 200, blank=True)
	time= models.CharField(max_length = 200, blank=True)
	time_of_registering_appointment=models.DateTimeField(auto_now = True,blank=True)
	prescription= models.CharField(max_length = 1000, blank=True)
	status= models.CharField(max_length = 200, default="pending")
	
	receptionist_response= models.CharField(max_length = 200, default="pending")
	receptionist_reason= models.CharField(max_length = 200, blank=True)
	
	doctor_response= models.CharField(max_length = 200, default="pending")
	doctor_reason= models.CharField(max_length = 200, blank=True)
	is_modify_by_doc= models.CharField(max_length = 200, default="none")
	
	
