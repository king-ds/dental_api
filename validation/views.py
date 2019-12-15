# Django
from django.shortcuts import render
from django.http import HttpResponse

# Django Rest
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Application
from authentication.serializers import *
from authentication.models import * 

class RetrieveClinicianUser(generics.RetrieveAPIView):
    lookup_field = 'student_number'
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

class RetrieveClinicalInstructor(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = ClinicalInstructor.objects.all()
    serializer_class = ClinicalInstructorSerializer

class RetrievePatient(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer