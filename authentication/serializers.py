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
    middle_initial = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    birthdate = serializers.DateField(required=True)
    religion = serializers.CharField(allow_blank=True, allow_null=True)
    marital_status = serializers.CharField(required=True)
    occupation = serializers.CharField(required=True)
    height = serializers.CharField(required=False, allow_null=True)
    weight = serializers.FloatField(required=False, allow_null=True)
    permanent_address = serializers.CharField(required=True)
    telephone_num = serializers.CharField(allow_blank=True, allow_null=True)
    phone_num = serializers.CharField(allow_blank=True, allow_null=True)
    email_address = serializers.EmailField(allow_blank=True, allow_null=True)
    emergency_full_name = serializers.CharField(required=False, allow_blank=True)
    relation_to_patient = serializers.CharField(required=True)
    emergency_phone_num = serializers.CharField(allow_blank=True, allow_null=True)
    emergency_address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    emergency_telephone_num = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Patient
        fields = ('id', 'username', 'first_name', 'middle_initial', 'last_name',
        'password', 'title', 'gender', 'birthdate', 'religion', 'marital_status',
        'occupation', 'height', 'weight', 'permanent_address',
        'telephone_num', 'phone_num', 'email_address', 'emergency_full_name',
        'relation_to_patient', 'emergency_phone_num', 'emergency_address', 
        'emergency_telephone_num', 'datetime_joined', 'has_doctor')