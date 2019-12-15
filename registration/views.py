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

class CreateClinician(generics.CreateAPIView):
    model = Clinician
    serializer_class = ClinicianSerializer

class CreateClinicalInstructor(generics.CreateAPIView):
    model = ClinicalInstructor
    serializer_class = ClinicalInstructorSerializer

class CreatePatient(generics.CreateAPIView):
    model = Patient
    serializer_class = PatientSerializer