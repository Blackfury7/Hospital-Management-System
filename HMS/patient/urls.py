from django.urls import path
from . import views


urlpatterns=[

path('basic_details/', views.patient_basic_details, name="patient_basic_details"),
path('medical_history/', views.show_medical_history, name="medical_history"),
path('prescription/', views.show_current_prescription, name="prescription"),
path('appointment_request/', views.appointment_request, name="prescription"),
# path('appointments/', views.show_current_appointments, name="appointments"),
path('payment_history/', views.show_payment_history, name="payment_history"),
path('list/', views.patient_list, name="patient_list"),

	


]