from django.urls import path
from . import views


urlpatterns=[

path('', views.home, name="home"),
path('dashboard/', views.doctor_dashboard, name="doctor_dashboard"),
path('list/', views.doctor_list, name="doctor_list"),
path('patient_list/', views.patient_list_under_doctor, name="patient_list_under_doctor"),
path('list_by_department/', views.doctor_list_by_department, name="doctor_list_by_department"),

	


]