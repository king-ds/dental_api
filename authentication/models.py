from django.db import models
# from track_record.models import *

class Clinician(models.Model):
    student_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    clinic_level = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    datetime_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class ClinicalInstructor(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    datetime_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Patient(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    has_doctor = models.BooleanField(default=False)
    datetime_assigned = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    religion = models.CharField(max_length=30, null=True)
    marital_status = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    height = models.CharField(max_length=10, null=True)
    weight = models.FloatField(null=True)
    permanent_address = models.TextField()
    telephone_num = models.CharField(max_length=10, null=True)
    phone_num = models.CharField(max_length=15, null=True)
    email_address = models.EmailField(blank=True, null=True)
    emergency_full_name = models.CharField(max_length=100)
    relation_to_patient = models.CharField(max_length=30)
    emergency_phone_num = models.CharField(max_length=15, null=True)
    emergency_telephone_num = models.CharField(max_length=10, null=True)
    emergency_address = models.TextField(null=True)
    # track_record = models.ForeignKey('track_record.TrackRecord', on_delete=models.CASCADE, blank=True, null=True)
    datetime_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)