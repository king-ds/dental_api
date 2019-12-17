from django.urls import path
from . import views

urlpatterns = [
    path('instructor-list/', views.InstructorList.as_view()),
    path('instructor-list/<int:id>', views.RetrieveInstructor.as_view()),
]