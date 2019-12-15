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

# Python
import secrets

# Create your views here.
def test(request):
    return HttpResponse('Hello World')

class ListClinicianUser(generics.ListAPIView):
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

"""
Function-based for authentication
"""

# For clinicians
@csrf_exempt
@api_view(["POST"])
def login_as_clinician(request):

    student_number = request.data.get('student_number')
    password = request.data.get('password')
    print(secrets.token_hex())

    isExist = Clinician.objects.filter(student_number=student_number, password=password).exists()

    if isExist:
        user = Clinician.objects.get(student_number=student_number, password=password)
        data = { 'message' : 'successful', 'id' : user.id, 'student_number' : user.student_number, 'first_name' : user.first_name,
        'last_name' : user.last_name, 'middle_name' : user.middle_name, 'token' : secrets.token_hex(), 'clinic_level' : user.clinic_level }
        status = HTTP_200_OK
    else:
        data = { 'message' : 'error' }
        status = HTTP_404_NOT_FOUND

    return Response(data, status=status)

# For clinical instructors
@csrf_exempt
@api_view(["POST"])
def login_as_instructor(request):
    username = request.data.get("username")
    password = request.data.get("password")

    isExist = ClinicalInstructor.objects.filter(username=username, password=password).exists()

    if isExist:
        user = ClinicalInstructor.objects.get(username=username, password=password)
        data = { 'message' : 'success', 'id' : user.id }
        status = HTTP_200_OK
    else:
        data = { 'message' : 'error' }
        status = HTTP_404_NOT_FOUND

    return Response(data, status=status)

# For patients
@csrf_exempt
@api_view(["POST"])
def login_as_patient(request):
    username = request.data.get("username")
    password = request.data.get("password")

    isExist = Patient.objects.filter(username=username, password=password).exists()

    if isExist:
        user = Patient.objects.get(username=username, password=password)
        data = { 'message' : 'success', 'id' : user.id }
        status = HTTP_200_OK
    else:
        data = { 'message' : 'error' }
        status = HTTP_404_NOT_FOUND

    return Response(data, status=status)