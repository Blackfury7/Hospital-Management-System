from django.url import path
from . import views


urlspatterns=[

path('doctor', doctor_registration, name="doctorRegistration"),
path('patient', patient_registration, name="patientRegistration"),
	


]