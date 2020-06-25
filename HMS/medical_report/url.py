from django.urls import path
from . import views


urlpatterns=[

path('add/', views.add_medical_report, name="add_medical_report"),

	


]