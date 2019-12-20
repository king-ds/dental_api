from django.urls import path
from . import views

urlpatterns = [
    path('update/patient/<int:id>', views.AssignPatient.as_view()),
    path('update/track-record/<int:id>', views.AssignTrackRecord.as_view()),
    path('update/patient-details/<int:id>', views.UpdatePatientDetails.as_view()),
    path('update/clinician-details/<int:id>', views.UpdateClinicianDetails.as_view())
]