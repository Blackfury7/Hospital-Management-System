from django.urls import path
from . import views


urlpatterns=[


path('patient/', views.patient_appointment, name="patient_appointment"),
path('receptionist/requests/', views.receptionist_appointment_requests, name="receptionist_appointment_requests"),

path('doctor/requests/', views.doctor_appointment_requests, name="doctor_appointment_requests"),
path('update_response/', views.updating_response_of_appointment, name="updating_response"),
path('doctor/appointment_details/', views.show_appointment_request_details, name="appointment_details"),
path('doctor/live_appointments_list/', views.doctor_live_appointments_list, name="doctor_live_appointments_list"),
path('doctor/live_appointment_details/', views.doctor_live_appointment_details, name="doctor_live_appointment_details"),



]