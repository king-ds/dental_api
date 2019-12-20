from django.urls import path
from . import views

urlpatterns = [
    path('track-record-list/<int:patient>', views.MyTrackRecord.as_view()),
    path('track-record/clinician-all-cdar/<int:clinician>', views.MyAllCDAR.as_view()),
    path('track-record/clinician-today-cdar/<int:clinician>', views.MyTodayCDAR.as_view()),
]