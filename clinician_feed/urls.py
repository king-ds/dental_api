from django.urls import path
from . import views

urlpatterns = [
    path('clinician-list/', views.ClinicianList.as_view()),
    path('clinician-list/<int:id>', views.RetrieveClinician.as_view()),
]