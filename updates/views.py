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
from updates.serializers import *

class AssignPatient(generics.UpdateAPIView):
    serializer_class = AssignPatientSerializer
    lookup_field = 'id'
    queryset = Patient.objects.filter(has_doctor=False)

class AssignTrackRecord(generics.UpdateAPIView):
    serializer_class = AssignTrackRecordSerializer
    lookup_field = 'id'
    queryset = TrackRecord.objects.filter(is_approved_instructor=False)