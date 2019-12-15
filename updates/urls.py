from django.urls import path
from . import views

urlpatterns = [
    path('update/patient/<int:id>', views.AssignPatient.as_view()),
    path('update/track-record/<int:id>', views.AssignTrackRecord.as_view()),
]