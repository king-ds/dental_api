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
from rest_framework import filters

# Application
from authentication.serializers import *
from authentication.models import * 
from track_record.serializers import *
from track_record.models import *

class PatientList(generics.ListAPIView):
    search_fields = ['last_name', 'first_name', 'middle_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Patient.objects.filter(has_doctor=False)
    serializer_class = PatientSerializer

class RetrievePatient(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class MyPatientTrackRecord(generics.ListAPIView):
    search_fields = ['id', 'patient__first_name', 'patient__middle_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MixTrackRecordSerializer

    def get_queryset(self):
        clinician_id = self.kwargs['clinician']
        return TrackRecord.objects.filter(clinician=clinician_id)