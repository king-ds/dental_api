from django.urls import path
from . import views

urlpatterns = [
    path('patients-list/', views.PatientList.as_view()),
    path('patients-list/<int:id>', views.RetrievePatient.as_view()),
    path('my-patients-list/<int:clinician>', views.MyPatientTrackRecord.as_view()),
]