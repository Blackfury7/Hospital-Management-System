from django.urls import path
from . import views


urlpatterns=[

path('doctor/', views.doctor_registration, name="doctorRegistration"),
path('patient/', views.patient_registration, name="patientRegistration"),
path('check_username/', views.check_username_already_exists, name="check_username"),

	


]