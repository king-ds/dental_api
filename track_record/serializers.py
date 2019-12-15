from authentication.models import *
from track_record.models import *
from rest_framework import serializers
from authentication.serializers import *

class AdditionalPersonalDataSerializer(serializers.ModelSerializer):
    chief_complaint = serializers.CharField(allow_blank=True)
    history_of_present_illness = serializers.CharField(allow_blank=True)

    class Meta:
        model = AdditionalPersonalData
        fields = "__all__"

class MedicalHistorySerializer(serializers.ModelSerializer):
    physician_care = serializers.BooleanField()
    hospitalization = serializers.CharField(allow_blank=True)
    allergies = serializers.CharField(allow_blank=True)
    illnesses = serializers.CharField(allow_blank=True)
    medications = serializers.CharField(allow_blank=True)
    childhood_disease_history = serializers.CharField(allow_blank=True)

    class Meta:
        model = MedicalHistory
        fields = "__all__"

class MedicalHealthQuestionnaireSerializer(serializers.ModelSerializer):
    others = serializers.CharField(allow_blank=True)

    class Meta:
        model = MedicalHealthQuestionnaire
        fields = "__all__"

class DentalChartSerializer(serializers.ModelSerializer):
    teeth_number = serializers.IntegerField(required=False, allow_null=True)
    kind = serializers.CharField(allow_blank=True)
    quadrant = serializers.IntegerField(required=False, allow_null=True)
    top = serializers.CharField(allow_blank=True, required=False)
    left = serializers.CharField(allow_blank=True, required=False)
    right = serializers.CharField(allow_blank=True, required=False)
    bottom = serializers.CharField(allow_blank=True, required=False)
    middle = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = DentalChart
        fields = "__all__"

class VitalSignSerializer(serializers.ModelSerializer):
    BP_1 = serializers.IntegerField(required=False)
    BP_2 = serializers.IntegerField(required=False)
    PR = serializers.FloatField(required=False)
    RR = serializers.FloatField(required=False)
    TEMP = serializers.FloatField(required=False)

    class Meta:
        model = VitalSign
        fields = "__all__"

class AllergiesSerializer(serializers.ModelSerializer):
    others = serializers.CharField(allow_blank=True)
    
    class Meta:
        model = Allergy
        fields = "__all__"

class FemaleSerializer(serializers.ModelSerializer):
    pregnant = serializers.IntegerField(required=False, allow_null=True)
    breast_feeding = serializers.IntegerField(required=False, allow_null=True)
    menopause = serializers.IntegerField(required=False, allow_null=True)
    under_hormone = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Female
        fields = "__all__"

class SocialHistorySerializer(serializers.ModelSerializer):
    kind_tobacco = serializers.CharField(allow_blank=True)
    often_tobacco = serializers.CharField(allow_blank=True)
    years_tobacco = serializers.CharField(allow_blank=True)
    stop_tobacco = serializers.CharField(allow_blank=True)
    kind_cigarettes = serializers.CharField(allow_blank=True)
    often_cigarettes = serializers.CharField(allow_blank=True)
    years_cigarettes = serializers.CharField(allow_blank=True)
    stop_cigarettes = serializers.CharField(allow_blank=True)
    kind_vape = serializers.CharField(allow_blank=True)
    often_vape = serializers.CharField(allow_blank=True)
    years_vape = serializers.CharField(allow_blank=True)
    stop_vape = serializers.CharField(allow_blank=True)
    kind_recreation = serializers.CharField(allow_blank=True)
    often_recreation = serializers.CharField(allow_blank=True)
    years_recreation = serializers.CharField(allow_blank=True)
    stop_recreation = serializers.CharField(allow_blank=True)
    kind_therapeutic = serializers.CharField(allow_blank=True)
    often_therapeutic = serializers.CharField(allow_blank=True)
    years_therapeutic = serializers.CharField(allow_blank=True)
    stop_therapeutic = serializers.CharField(allow_blank=True)
    kind_alcoholic = serializers.CharField(allow_blank=True)
    often_alcoholic = serializers.CharField(allow_blank=True)
    years_alcoholic = serializers.CharField(allow_blank=True)
    stop_alcoholic = serializers.CharField(allow_blank=True)
    
    class Meta:
        model = SocialHistory
        fields = "__all__"

class DentalHistorySerializer(serializers.ModelSerializer):
    freq_dental_visit = serializers.CharField(allow_blank=True)
    proc_last_visit = serializers.CharField(allow_blank=True)
    exposure_anesthesia = serializers.CharField(allow_blank=True)
    complications_dental = serializers.CharField(allow_blank=True)
    brush = serializers.IntegerField(required=False)
    floss = serializers.IntegerField(required=False)
    rinse = serializers.IntegerField(required=False)
    relevant_smile = serializers.CharField(allow_blank=True)
    relevant_extraction = serializers.CharField(allow_blank=True)
    relevant_orthodomic = serializers.CharField(allow_blank=True)
    relevant_gums = serializers.CharField(allow_blank=True)
    relevant_cold = serializers.CharField(allow_blank=True)
    relevant_denture = serializers.CharField(allow_blank=True)
    relevant_periodental = serializers.CharField(allow_blank=True)
    relevant_bleed = serializers.CharField(allow_blank=True)
    relevant_jaw_pain = serializers.CharField(allow_blank=True)
    relevant_catch = serializers.CharField(allow_blank=True)
    date_last_visit = serializers.DateField(required=False)

    class Meta:
        model = DentalHistory
        fields = "__all__"

class NormalAbnormalSerializer(serializers.ModelSerializer):
    skin_desc = serializers.CharField(allow_blank=True)
    eyes_desc = serializers.CharField(allow_blank=True)
    neck_desc = serializers.CharField(allow_blank=True)
    TMD_desc = serializers.CharField(allow_blank=True)
    lymph_nodes_desc = serializers.CharField(allow_blank=True)
    lips_desc = serializers.CharField(allow_blank=True)
    buccal_mucosa_desc = serializers.CharField(allow_blank=True)
    vestibule_desc = serializers.CharField(allow_blank=True)
    alveolar_ridge_desc = serializers.CharField(allow_blank=True)
    hard_palate_desc = serializers.CharField(allow_blank=True)
    oro_pharynx_desc = serializers.CharField(allow_blank=True)
    tongue_desc = serializers.CharField(allow_blank=True)
    mouth_floor_desc = serializers.CharField(allow_blank=True)
    salivary_glands_desc = serializers.CharField(allow_blank=True)

    class Meta:
        model = NormalAbnormal
        fields = "__all__"

class OcclusionSerializer(serializers.ModelSerializer):
    occlusion = serializers.CharField(allow_blank=True)
    other_occlusal = serializers.CharField(allow_blank=True)
    oral_habits = serializers.CharField(allow_blank=True)
    plaque = serializers.CharField(allow_blank=True)
    enamel = serializers.CharField(allow_blank=True)

    class Meta:
        model = Occlusion
        fields = "__all__"

class GingivaSerializer(serializers.ModelSerializer):
    attached_gingiva = serializers.CharField(allow_blank=True)
    frenular_attachment = serializers.CharField(allow_blank=True)
    color = serializers.CharField(allow_blank=True)
    consistency = serializers.CharField(allow_blank=True)
    contour = serializers.CharField(allow_blank=True)
    texture = serializers.CharField(allow_blank=True)

    class Meta:
        model = Gingiva
        fields = "__all__"

# class PeriodontalDiagnosisSerializer(serializers.ModelSerializer):
#     asa_type = 

class TrackRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackRecord
        fields = "__all__"

class MixTrackRecordSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(required=False)
    clinician = ClinicianSerializer(required=False)
    additional_personal_data = AdditionalPersonalDataSerializer(required=False)
    medical_history = MedicalHistorySerializer(required=False)
    medical_health_questionnaire = MedicalHealthQuestionnaireSerializer(required=False)
    female = FemaleSerializer(required=False)
    allergy = AllergiesSerializer(required=False)

    class Meta:
        model = TrackRecord
        fields = ("additional_personal_data", "medical_history", "medical_health_questionnaire",  
                "allergy", "patient", "clinician", "female", "id", "is_approved_instructor", "url")

    def update(self, instance, validated_data):

        # Complaint
        try:

            additional_personal_data_data = validated_data.pop('additional_personal_data')
            additional_personal_data = instance.additional_personal_data
            additional_personal_data.chief_complaint = additional_personal_data_data.get('chief_complaint', additional_personal_data.chief_complaint)
            additional_personal_data.history_of_present_illness = additional_personal_data_data.get('history_of_present_illness', additional_personal_data.history_of_present_illness)

            additional_personal_data.save()
        except:
            pass

        # Medical History
        try:
            medical_history_data = validated_data.pop('medical_history')
            medical_history = instance.medical_history
            medical_history.physician_care = medical_history_data.get('physician_care', medical_history.physician_care)
            medical_history.hospitalization = medical_history_data.get('hospitalization', medical_history.hospitalization)
            medical_history.allergies = medical_history_data.get('allergies', medical_history.allergies)
            medical_history.illnesses = medical_history_data.get('illnesses', medical_history.illnesses)
            medical_history.medications = medical_history_data.get('medications', medical_history.medications)
            medical_history.childhood_disease_history = medical_history_data.get('childhood_disease_history', medical_history.childhood_disease_history)
            
            medical_history.save()
        except:
            pass

        # Medical Health Questionnaire
        try :
            medical_health_questionnaire_data = validated_data.pop('medical_health_questionnaire')
            medical_health_questionnaire = instance.medical_health_questionnaire
            medical_health_questionnaire.high_blood_pressure = medical_health_questionnaire_data.get('high_blood_pressure', medical_health_questionnaire.high_blood_pressure)
            medical_health_questionnaire.diabetes = medical_health_questionnaire_data.get('diabetes', medical_health_questionnaire.diabetes)
            medical_health_questionnaire.osteoporosis = medical_health_questionnaire_data.get('osteoporosis', medical_health_questionnaire.osteoporosis)  
            medical_health_questionnaire.herpes = medical_health_questionnaire_data.get('herpes', medical_health_questionnaire.herpes)
            medical_health_questionnaire.radiation_treatments = medical_health_questionnaire_data.get('radiation_treatments', medical_health_questionnaire.radiation_treatments)
            medical_health_questionnaire.chemotherapy = medical_health_questionnaire_data.get('chemotherapy', medical_health_questionnaire.chemotherapy)
            medical_health_questionnaire.artificial_heart_valves = medical_health_questionnaire_data.get('artificial_heart_valves', medical_health_questionnaire.artificial_heart_valves)
            medical_health_questionnaire.pacemaker = medical_health_questionnaire_data.get('pacemaker', medical_health_questionnaire.pacemaker)
            medical_health_questionnaire.angioplasty = medical_health_questionnaire_data.get('angioplasty', medical_health_questionnaire.angioplasty)
            medical_health_questionnaire.stroke = medical_health_questionnaire_data.get('stroke', medical_health_questionnaire.stroke)
            medical_health_questionnaire.angina_pectrosis = medical_health_questionnaire_data.get('angina_pectrosis', medical_health_questionnaire.angina_pectrosis)
            medical_health_questionnaire.frequent_high_fever = medical_health_questionnaire_data.get('frequent_high_fever', medical_health_questionnaire.frequent_high_fever)
            medical_health_questionnaire.sinusitis = medical_health_questionnaire_data.get('sinusitis', medical_health_questionnaire.sinusitis)
            medical_health_questionnaire.asthma = medical_health_questionnaire_data.get('asthma', medical_health_questionnaire.asthma)
            medical_health_questionnaire.breathing_problems = medical_health_questionnaire_data.get('breathing_problems', medical_health_questionnaire.breathing_problems)
            medical_health_questionnaire.afternoon_fever = medical_health_questionnaire_data.get('afternoon_fever', medical_health_questionnaire.afternoon_fever)
            medical_health_questionnaire.chronic_cough = medical_health_questionnaire_data.get('chronic_cough', medical_health_questionnaire.chronic_cough)
            medical_health_questionnaire.bloody_sputum = medical_health_questionnaire_data.get('bloody_sputum', medical_health_questionnaire.bloody_sputum)
            medical_health_questionnaire.tuberculosis = medical_health_questionnaire_data.get('tuberculosis', medical_health_questionnaire.tuberculosis)
            medical_health_questionnaire.frequent_heartaches = medical_health_questionnaire_data.get('frequent_heartaches', medical_health_questionnaire.frequent_heartaches)
            medical_health_questionnaire.visual_impairment = medical_health_questionnaire_data.get('visual_impairment', medical_health_questionnaire.visual_impairment)
            medical_health_questionnaire.hearing_impairment = medical_health_questionnaire_data.get('hearing_impairment', medical_health_questionnaire.hearing_impairment)
            medical_health_questionnaire.athritis = medical_health_questionnaire_data.get('athritis', medical_health_questionnaire.athritis)
            medical_health_questionnaire.pain_in_joints = medical_health_questionnaire_data.get('pain_in_joints', medical_health_questionnaire.pain_in_joints)
            medical_health_questionnaire.tumors = medical_health_questionnaire_data.get('tumors', medical_health_questionnaire.tumors)
            medical_health_questionnaire.goiter = medical_health_questionnaire_data.get('goiter', medical_health_questionnaire.goiter)
            medical_health_questionnaire.frequent_thirst = medical_health_questionnaire_data.get('frequent_thirst', medical_health_questionnaire.frequent_thirst)
            medical_health_questionnaire.frequent_hunger = medical_health_questionnaire_data.get('frequent_hunger', medical_health_questionnaire.frequent_hunger)
            medical_health_questionnaire.frequent_urination = medical_health_questionnaire_data.get('frequent_urination', medical_health_questionnaire.frequent_urination)
            medical_health_questionnaire.sudden_weight_loss = medical_health_questionnaire_data.get('sudden_weight_loss', medical_health_questionnaire.sudden_weight_loss)
            medical_health_questionnaire.abdominal_discomfort = medical_health_questionnaire_data.get('abdominal_discomfort', medical_health_questionnaire.abdominal_discomfort)
            medical_health_questionnaire.acidic_reflux = medical_health_questionnaire_data.get('acidic_reflux', medical_health_questionnaire.acidic_reflux)
            medical_health_questionnaire.bleeding_bruining_easily = medical_health_questionnaire_data.get('bleeding_bruining_easily', medical_health_questionnaire.bleeding_bruining_easily)
            medical_health_questionnaire.recreational_drugs = medical_health_questionnaire_data.get('recreational_drugs', medical_health_questionnaire.recreational_drugs)
            medical_health_questionnaire.steroid_therapy = medical_health_questionnaire_data.get('steroid_therapy', medical_health_questionnaire.steroid_therapy)
            medical_health_questionnaire.blood = medical_health_questionnaire_data.get('blood', medical_health_questionnaire.blood)
            medical_health_questionnaire.pain_upon_urination = medical_health_questionnaire_data.get('pain_upon_urination', medical_health_questionnaire.pain_upon_urination)
            medical_health_questionnaire.kidney_liver_problems = medical_health_questionnaire_data.get('kidney_liver_problems', medical_health_questionnaire.kidney_liver_problems)
            medical_health_questionnaire.hepatitis = medical_health_questionnaire_data.get('hepatitis', medical_health_questionnaire.hepatitis)
            medical_health_questionnaire.sexually_transmitted_disease = medical_health_questionnaire_data.get('sexually_transmitted_disease', medical_health_questionnaire.sexually_transmitted_disease)
            medical_health_questionnaire.hiv_positive = medical_health_questionnaire_data.get('hiv_positive', medical_health_questionnaire.hiv_positive)
            medical_health_questionnaire.depression = medical_health_questionnaire_data.get('depression', medical_health_questionnaire.depression)
            medical_health_questionnaire.fainting_spells = medical_health_questionnaire_data.get('fainting_spells', medical_health_questionnaire.fainting_spells)
            medical_health_questionnaire.heart_attack  = medical_health_questionnaire_data.get('heart_attack', medical_health_questionnaire.heart_attack)
            medical_health_questionnaire.empyema  = medical_health_questionnaire_data.get('empyema', medical_health_questionnaire.empyema)
            medical_health_questionnaire.swollen_ankles  = medical_health_questionnaire_data.get('swollen_ankles', medical_health_questionnaire.swollen_ankles)
            medical_health_questionnaire.others = medical_health_questionnaire_data.get('others', medical_health_questionnaire.others)

            medical_health_questionnaire.save()
        except:
            pass
        
        # Allergies
        try:
            allergies_data = validated_data.pop('allergy')
            allergies = instance.allergy
            allergies.aspirin = allergies_data.get('aspirin', allergies.aspirin)
            allergies.penicillin = allergies_data.get('penicillin', allergies.penicillin)
            allergies.latex = allergies_data.get('latex', allergies.latex)
            allergies.metal = allergies_data.get('metal', allergies.metal)
            allergies.none = allergies_data.get('none', allergies.none)
            allergies.others = allergies_data.get('others', allergies.others)

            allergies.save()
        except:
            pass

        # Female
        try:
            female_data = validated_data.pop('female')
            female = instance.female
            female.is_pregnant = female_data.get('is_pregnant', female.is_pregnant)
            female.is_breast_feeding = female_data.get('is_breast_feeding', female.is_breast_feeding)
            female.is_menopause = female_data.get('is_menopause', female.is_menopause)
            female.is_under_hormone = female_data.get('is_under_hormone', female.is_under_hormone)
            female.pregnant = female_data.get('pregnant', female.pregnant)
            female.breast_feeding = female_data.get('breast_feeding', female.breast_feeding)
            female.menopause = female_data.get('menopause', female.menopause)
            female.under_hormone = female_data.get('under_hormone', female.under_hormone)

            female.save()
        except:
            pass

        return instance