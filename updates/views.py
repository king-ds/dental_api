# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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
from rest_framework.views import APIView

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

class UpdatePatientDetails(APIView):

    def patch(self, request, *args, **kwargs):
        patient = get_object_or_404(Patient, pk=kwargs['id'])
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            patient = serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

class UpdateClinicianDetails(APIView):

    def patch(self, request, *args, **kwargs):
        clinician = get_object_or_404(Clinician, pk=kwargs['id'])
        serializer = ClinicianSerializer(clinician, data=request.data, partial=True)
        if serializer.is_valid():
            clinician = serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

