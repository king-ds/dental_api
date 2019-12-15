from django.urls import path
from . import views

urlpatterns = [
    path('register/clinician', views.CreateClinician.as_view()),
    path('register/instructor', views.CreateClinicalInstructor.as_view()),
    path('register/patient', views.CreatePatient.as_view()),
]