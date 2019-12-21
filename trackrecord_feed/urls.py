from django.urls import path
from . import views

urlpatterns = [
    path('track-record-list/<int:patient>', views.MyTrackRecord.as_view()),
    path('track-record/clinician-all-cdar/<int:clinician>', views.MyAllCDAR.as_view()),
    path('track-record/clinician-today-cdar/<int:clinician>', views.MyTodayCDAR.as_view()),
    path('track-record/instructor-all-cdar/<int:clinical_instructor>', views.InstructorAllCDAR.as_view()),
    path('track-record/instructor-today-cdar/<int:clinical_instructor>', views.InstructorTodayCDAR.as_view()),
    path('track-record/instructor-track-records/<int:clinical_instructor>', views.InstructorTrackRecordFeed.as_view()),
]