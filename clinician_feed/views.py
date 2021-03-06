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
class ClinicianList(generics.ListAPIView):
    search_fields = ['last_name', 'first_name', 'middle_name', 'student_number']
    filter_backends = (filters.SearchFilter,)
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

class RetrieveClinician(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer