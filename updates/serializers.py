from authentication.models import *
from track_record.models import *
from rest_framework import serializers

class AssignPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['has_doctor', 'datetime_assigned']

class AssignTrackRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackRecord
        fields = "__all__"