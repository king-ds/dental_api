from django.db import models

class Clinician(models.Model):
    student_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    clinic_level = models.CharField(max_length=10)
    datetime_joined = models.DateTimeField(auto_now_add=True)
    # CDAR = models.ForeignKey()
    # track_record = models.ForeignKey()

    def __str__(self):
        return str(self.id)

class ClinicalInstructor(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # CDAR = models.ForeignKey()

    def __str__(self):
        return str(self.id)

class Patient(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    has_doctor = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(Clinician, blank=True, null=True, on_delete=models.CASCADE)
    datetime_assigned = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    religion = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    number_of_kids = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    permanent_address = models.TextField()
    telephone_num = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=15)
    email_address = models.EmailField(blank=True)
    emergency_first_name = models.CharField(max_length=100)
    emergency_middle_name = models.CharField(max_length=100)
    emergency_last_name = models.CharField(max_length=100)
    relation_to_patient = models.CharField(max_length=30)
    emergency_phone_num = models.CharField(max_length=15)
    emergency_telephone_num = models.CharField(max_length=10)
    emergency_address = models.TextField()
    datetime_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)