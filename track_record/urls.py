from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('track-record', views.MixTrackRecord)

urlpatterns = [
    path('', include(router.urls)),
    path('track-record/additional-personal-data', views.CreateAdditionalPersonalData.as_view()),
    path('track-record/medical-history', views.CreateMedicalHistory.as_view()),
    path('track-record/medical-history-questionnaire', views.CreateMedicalHistoryQuestionnaire.as_view()),
    path('track-record/vital-sign', views.CreateVitalSign.as_view()),
    path('track-record/track-record', views.CreateTrackRecord.as_view()),
    path('track-record/allergies', views.CreatAllergies.as_view()),
    path('track-record/female', views.CreateFemale.as_view()),
    path('track-record/social-history', views.CreateSocialHistory.as_view()),
    path('track-record/dental-history', views.CreateDentalHistory.as_view()),
    path('track-record/dental-chart', views.CreateDentalChart.as_view()),
    path('track-record/oral-assessment', views.CreateOralAssessment.as_view()),
    path('track-record/occlusion', views.CreateOcclusion.as_view()),
    path('track-record/gingiva', views.CreateGingiva.as_view()),
    path('track-record/treatment-record', views.CreateTreatmentRecord.as_view()),
    path('track-record/vital-sign/<int:track_record>', views.VitalSignFeed.as_view()),
    path('track-record/treatment-record/<int:track_record>', views.TreatmentRecordFeed.as_view()),
    path('track-record/dental-chart/<int:track_record>', views.DentalChartFeed.as_view()),
    path('track-record/dental-chart-q1/<int:track_record>', views.Q1DentalChartFeed.as_view()),
    path('track-record/dental-chart-q2/<int:track_record>', views.Q2DentalChartFeed.as_view()),
    path('track-record/dental-chart-q3/<int:track_record>', views.Q3DentalChartFeed.as_view()),
    path('track-record/dental-chart-q4/<int:track_record>', views.Q4DentalChartFeed.as_view()),
    path('track-record/vital-sign-detail/<int:id>', views.VitalSignDetailView.as_view()),
    path('track-record/dental-chart-detail/<int:id>', views.DentalChartDetailView.as_view()),
]