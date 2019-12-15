from django.urls import path
from . import views

urlpatterns = [
    path('clinicians/<str:student_number>', views.RetrieveClinicianUser.as_view()),
    path('clinical-instructors/<str:username>', views.RetrieveClinicalInstructor.as_view()),
    path('patients/<str:username>', views.RetrievePatient.as_view()),
]