# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Django Rest
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView

# Application
from track_record.serializers import *
from track_record.models import * 


class CreateAdditionalPersonalData(generics.CreateAPIView):
    model = AdditionalPersonalData
    serializer_class = AdditionalPersonalDataSerializer

class CreateMedicalHistory(generics.CreateAPIView):
    model = MedicalHistory
    serializer_class = MedicalHistorySerializer

class CreateDentalChart(generics.CreateAPIView):
    model = DentalChart
    serializer_class = DentalChartSerializer

class CreateMedicalHistoryQuestionnaire(generics.CreateAPIView):
    model = MedicalHealthQuestionnaire
    serializer_class = MedicalHealthQuestionnaireSerializer

class CreateVitalSign(generics.CreateAPIView):
    model = VitalSign
    serializer_class = VitalSignSerializer

class CreateFemale(generics.CreateAPIView):
    model = Female
    serializer_class = FemaleSerializer

class CreateSocialHistory(generics.CreateAPIView):
    model = SocialHistory
    serializer_class = SocialHistorySerializer

class CreateDentalHistory(generics.CreateAPIView):
    model = DentalHistory
    serializer_class = DentalHistorySerializer

class CreateOralAssessment(generics.CreateAPIView):
    model = OralAssessment
    serializer_class = OralAssessmentSerializer

class CreateOcclusion(generics.CreateAPIView):
    model = Occlusion
    serializer_class = OcclusionSerializer

class CreateGingiva(generics.CreateAPIView):
    model = Gingiva
    serializer_class = GingivaSerializer

class CreateTrackRecord(generics.CreateAPIView):
    model = TrackRecord
    serializer_class = TrackRecordSerializer

class CreatAllergies(generics.CreateAPIView):
    model = Allergy
    serializer_class = AllergiesSerializer

class CreateTreatmentRecord(generics.CreateAPIView):
    model = TreatmentRecord
    serializer_class = TreatmentRecordSerializer

class CreateCDAR(generics.CreateAPIView):
    model = CDAR
    serializer_class = CDARSerializer

class MixTrackRecord(viewsets.ModelViewSet):
    queryset = TrackRecord.objects.all()
    serializer_class = MixTrackRecordSerializer

class TreatmentRecordFeed(generics.ListAPIView):
    serializer_class = MixTreatmentRecordSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return TreatmentRecord.objects.filter(track_record=track_record_id)

class VitalSignFeed(generics.ListAPIView):
    serializer_class = VitalSignSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return VitalSign.objects.filter(track_record=track_record_id)

class DentalChartFeed(generics.ListAPIView):
    serializer_class = DentalChartSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return DentalChart.objects.filter(track_record=track_record_id)

class Q1DentalChartFeed(generics.ListAPIView):
    serializer_class = DentalChartSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return DentalChart.objects.filter(track_record=track_record_id, quadrant=1).order_by('teeth_number')

class Q2DentalChartFeed(generics.ListAPIView):
    serializer_class = DentalChartSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return DentalChart.objects.filter(track_record=track_record_id, quadrant=2).order_by('teeth_number')

class Q3DentalChartFeed(generics.ListAPIView):
    serializer_class = DentalChartSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return DentalChart.objects.filter(track_record=track_record_id, quadrant=3).order_by('teeth_number')

class Q4DentalChartFeed(generics.ListAPIView):
    serializer_class = DentalChartSerializer

    def get_queryset(self):
        track_record_id = self.kwargs['track_record']
        return DentalChart.objects.filter(track_record=track_record_id, quadrant=4).order_by('teeth_number')

class VitalSignDetailView(APIView):
    
    def patch(self, request, *args, **kwargs):
        vital_sign = get_object_or_404(VitalSign, pk=kwargs['id'])
        serializer = VitalSignSerializer(vital_sign, data=request.data, partial=True)
        if serializer.is_valid():
            vital_sign = serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        vital_sign = get_object_or_404(VitalSign, pk=kwargs['id'])
        vital_sign.delete()
        return Response("Successfully Deleted", status=HTTP_204_NO_CONTENT)

class DentalChartDetailView(APIView):

    def patch(self, request, *args, **kwargs):
        dental_chart = get_object_or_404(DentalChart, pk=kwargs['id'])
        serializer = DentalChartSerializer(dental_chart, data=request.data, partial=True)
        if serializer.is_valid():
            dental_chart = serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

class TreatmentRecordDetailView(APIView):

    def patch(self, request, *args, **kwargs):
        treatment_record = get_object_or_404(TreatmentRecord, pk=kwargs['id'])
        serializer = TreatmentRecordSerializer(treatment_record, data=request.data, partial=True)
        if serializer.is_valid():
            treatment_record = serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

class CDARDetailView(APIView):

    def patch(self, request, *args, **kwargs):
        cdar = get_object_or_404(CDAR, pk=kwargs['id'])
        serializer = CDARSerializer(cdar, data=request.data, partial=True)
        if serializer.is_valid():
            cdar = serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)