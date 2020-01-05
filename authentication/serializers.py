from authentication.models import *
from rest_framework import serializers

class ClinicianSerializer(serializers.ModelSerializer):
    student_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    clinic_level = serializers.CharField(required=True)

    class Meta:
        model = Clinician
        fields = ('id', 'student_number', 'first_name', 'middle_name', 'last_name', 'password', 'clinic_level', 'datetime_joined')

class ClinicalInstructorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = ClinicalInstructor
        fields = ('id', 'username', 'first_name', 'middle_name', 'last_name', 'password', 'datetime_joined')

class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    birthdate = serializers.DateField(required=True)
    religion = serializers.CharField(allow_blank=True)
    marital_status = serializers.CharField(required=True)
    occupation = serializers.CharField(required=True)
    number_of_kids = serializers.IntegerField(required=True)
    height = serializers.CharField(required=True)
    weight = serializers.FloatField(required=True)
    permanent_address = serializers.CharField(required=True)
    telephone_num = serializers.CharField(allow_blank=True)
    phone_num = serializers.CharField(allow_blank=True)
    email_address = serializers.EmailField(allow_blank=True)
    emergency_first_name = serializers.CharField(required=True)
    emergency_middle_name = serializers.CharField(required=True)
    emergency_last_name = serializers.CharField(required=True)
    relation_to_patient = serializers.CharField(required=True)
    emergency_phone_num = serializers.CharField(allow_blank=True)
    emergency_address = serializers.CharField(required=True)
    emergency_telephone_num = serializers.CharField(allow_blank=True)

    class Meta:
        model = Patient
        fields = ('id', 'username', 'first_name', 'middle_name', 'last_name',
        'password', 'title', 'gender', 'birthdate', 'religion', 'marital_status',
        'occupation', 'number_of_kids', 'height', 'weight', 'permanent_address',
        'telephone_num', 'phone_num', 'email_address', 'emergency_first_name',
        'emergency_middle_name', 'emergency_last_name', 'relation_to_patient', 
        'emergency_phone_num', 'emergency_address', 'emergency_telephone_num', 'datetime_joined')