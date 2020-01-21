# Python
from datetime import date

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

# Create your views here.
# class MyTrackRecord(generics.ListAPIView):
#     search_fields = ['id']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = MixTrackRecordSerializer

#     def get_queryset(self):
#         patient_id = self.kwargs['patient']
#         return TrackRecord.objects.filter(patient=patient_id)

class MyTrackRecord(generics.RetrieveAPIView):
    lookup_field = 'patient'
    serializer_class = MixTrackRecordSerializer
    queryset = TrackRecord.objects.all()

class MyAllCDAR(generics.ListAPIView):
    search_fields = ['procedure', 'id', 'clinician__last_name', 'clinician__first_name', 
                'patient__last_name', 'patient__first_name', 'clinical_instructor__first_name', 
                'clinical_instructor__last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MixCDARSerializer

    def get_queryset(self):
        clinician_id = self.kwargs['clinician']
        return CDAR.objects.filter(clinician=clinician_id)

class MyTodayCDAR(generics.ListAPIView):
    search_fields = ['procedure', 'id', 'clinician__last_name', 'clinician__first_name', 
                    'patient__last_name', 'patient__first_name', 'clinical_instructor__first_name', 
                    'clinical_instructor__last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MixCDARSerializer

    def get_queryset(self):
        clinician_id = self.kwargs['clinician']
        return CDAR.objects.filter(clinician=clinician_id, date=date.today())

class InstructorAllCDAR(generics.ListAPIView):
    search_fields = ['procedure', 'id', 'clinician__last_name', 'clinician__first_name', 
                'patient__last_name', 'patient__first_name', 'clinical_instructor__first_name', 
                'clinical_instructor__last_name', 'date']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MixCDARSerializer

    def get_queryset(self):
        instructor_id = self.kwargs['clinical_instructor']
        return CDAR.objects.filter(clinical_instructor=instructor_id).order_by('-date')

class InstructorTodayCDAR(generics.ListAPIView):
    search_fields = ['procedure', 'id', 'clinician__last_name', 'clinician__first_name', 
                    'patient__last_name', 'patient__first_name', 'clinical_instructor__first_name', 
                    'clinical_instructor__last_name', 'date']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MixCDARSerializer

    def get_queryset(self):
        instructor_id = self.kwargs['clinical_instructor']
        return CDAR.objects.filter(clinical_instructor=instructor_id, date=date.today()).order_by('-id')

class InstructorTrackRecordFeed(generics.ListAPIView):
    search_fields = ['id', 'patient__first_name', 'patient__last_name', 'clinician__last_name',
                    'clinician__first_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MixTrackRecordSerializer

    def get_queryset(self):
        instructor_id = self.kwargs['clinical_instructor']
        return TrackRecord.objects.filter(clinical_instructor=instructor_id)