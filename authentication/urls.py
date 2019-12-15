from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('users', views.ListClinicianUser.as_view()),
    path('authenticate/clinicians', views.login_as_clinician, name='login_as_clinician'),
    path('authenticate/instructors', views.login_as_instructor, name='login_as_instructor'),
    path('authenticate/patients', views.login_as_patient, name='login_as_patient')
]