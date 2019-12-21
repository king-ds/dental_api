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

class TreatmentRecordSerializer(serializers.ModelSerializer):
    procedure = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = TreatmentRecord
        fields = "__all__"

class CDARSerializer(serializers.ModelSerializer):
    procedure = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = CDAR
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
    kind_tobacco = serializers.CharField(allow_blank=True, required=False)
    often_tobacco = serializers.CharField(allow_blank=True, required=False)
    years_tobacco = serializers.CharField(allow_blank=True, required=False)
    stop_tobacco = serializers.CharField(allow_blank=True, required=False)
    kind_cigarettes = serializers.CharField(allow_blank=True, required=False)
    often_cigarettes = serializers.CharField(allow_blank=True, required=False)
    years_cigarettes = serializers.CharField(allow_blank=True, required=False)
    stop_cigarettes = serializers.CharField(allow_blank=True, required=False)
    kind_vape = serializers.CharField(allow_blank=True, required=False)
    often_vape = serializers.CharField(allow_blank=True, required=False)
    years_vape = serializers.CharField(allow_blank=True, required=False)
    stop_vape = serializers.CharField(allow_blank=True, required=False)
    kind_recreation = serializers.CharField(allow_blank=True, required=False)
    often_recreation = serializers.CharField(allow_blank=True, required=False)
    years_recreation = serializers.CharField(allow_blank=True, required=False)
    stop_recreation = serializers.CharField(allow_blank=True, required=False)
    kind_therapeutic = serializers.CharField(allow_blank=True, required=False)
    often_therapeutic = serializers.CharField(allow_blank=True, required=False)
    years_therapeutic = serializers.CharField(allow_blank=True, required=False)
    stop_therapeutic = serializers.CharField(allow_blank=True, required=False)
    kind_alcoholic = serializers.CharField(allow_blank=True, required=False)
    often_alcoholic = serializers.CharField(allow_blank=True, required=False)
    years_alcoholic = serializers.CharField(allow_blank=True, required=False)
    stop_alcoholic = serializers.CharField(allow_blank=True, required=False)
    
    class Meta:
        model = SocialHistory
        fields = "__all__"

class DentalHistorySerializer(serializers.ModelSerializer):
    freq_dental_visit = serializers.CharField(allow_blank=True, required=False)
    proc_last_visit = serializers.CharField(allow_blank=True, required=False)
    exposure_anesthesia = serializers.CharField(allow_blank=True, required=False)
    complications_dental = serializers.CharField(allow_blank=True, required=False)
    brush = serializers.IntegerField(required=False, allow_null=True)
    floss = serializers.IntegerField(required=False, allow_null=True)
    rinse = serializers.IntegerField(required=False, allow_null=True)
    relevant_smile = serializers.CharField(allow_blank=True, required=False)
    relevant_extraction = serializers.CharField(allow_blank=True, required=False)
    relevant_orthodomic = serializers.CharField(allow_blank=True, required=False)
    relevant_bled = serializers.CharField(allow_blank=True, required=False)
    relevant_gums = serializers.CharField(allow_blank=True, required=False)
    relevant_cold = serializers.CharField(allow_blank=True, required=False)
    relevant_denture = serializers.CharField(allow_blank=True, required=False)
    relevant_periodental = serializers.CharField(allow_blank=True, required=False)
    relevant_bleed = serializers.CharField(allow_blank=True, required=False)
    relevant_jaw_pain = serializers.CharField(allow_blank=True, required=False)
    relevant_catch = serializers.CharField(allow_blank=True, required=False)
    date_last_visit = serializers.DateField(required=False)

    class Meta:
        model = DentalHistory
        fields = "__all__"

class OralAssessmentSerializer(serializers.ModelSerializer):
    skin_desc = serializers.CharField(allow_blank=True, required=False)
    eyes_desc = serializers.CharField(allow_blank=True, required=False)
    neck_desc = serializers.CharField(allow_blank=True, required=False)
    TMD_desc = serializers.CharField(allow_blank=True, required=False)
    lymph_nodes_desc = serializers.CharField(allow_blank=True, required=False)
    lips_desc = serializers.CharField(allow_blank=True, required=False)
    buccal_mucosa_desc = serializers.CharField(allow_blank=True, required=False)
    vestibule_desc = serializers.CharField(allow_blank=True, required=False)
    alveolar_ridge_desc = serializers.CharField(allow_blank=True, required=False)
    hard_palate_desc = serializers.CharField(allow_blank=True, required=False)
    oro_pharynx_desc = serializers.CharField(allow_blank=True, required=False)
    tongue_desc = serializers.CharField(allow_blank=True, required=False)
    mouth_floor_desc = serializers.CharField(allow_blank=True, required=False)
    salivary_glands_desc = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = OralAssessment
        fields = "__all__"

class OcclusionSerializer(serializers.ModelSerializer):
    occlusion_class = serializers.CharField(allow_blank=True, required=False)
    other_occlusal = serializers.CharField(allow_blank=True, required=False)
    oral_habits = serializers.CharField(allow_blank=True, required=False)
    plaque = serializers.CharField(allow_blank=True, required=False)
    generalized_desc = serializers.CharField(allow_blank=True, required=False)
    localized_desc = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Occlusion
        fields = "__all__"

class GingivaSerializer(serializers.ModelSerializer):
    attached_gingiva = serializers.CharField(allow_blank=True, required=False)
    frenular_attachment = serializers.CharField(allow_blank=True, required=False)
    radiographic_stage = serializers.CharField(allow_blank=True, required=False)
    radiographic_hv = serializers.CharField(allow_blank=True, required=False)
    radiographic_gl = serializers.CharField(allow_blank=True, required=False)
    color = serializers.CharField(allow_blank=True, required=False)
    consistency = serializers.CharField(allow_blank=True, required=False)
    contour = serializers.CharField(allow_blank=True, required=False)
    texture = serializers.CharField(allow_blank=True, required=False)

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
    clinical_instructor = ClinicalInstructorSerializer(required=False)
    additional_personal_data = AdditionalPersonalDataSerializer(required=False)
    medical_history = MedicalHistorySerializer(required=False)
    medical_health_questionnaire = MedicalHealthQuestionnaireSerializer(required=False)
    female = FemaleSerializer(required=False)
    allergy = AllergiesSerializer(required=False)
    oral_assessment = OralAssessmentSerializer(required=False)
    occlusion = OcclusionSerializer(required=False)
    social_history = SocialHistorySerializer(required=False)
    dental_history = DentalHistorySerializer(required=False)
    gingiva = GingivaSerializer(required=False)

    class Meta:
        model = TrackRecord
        fields = ("additional_personal_data", "medical_history", "medical_health_questionnaire",  
                "allergy", "patient", "clinician", "female", "social_history", "oral_assessment", 
                "occlusion", "dental_history", "id", "is_approved_instructor", "is_approved_patient", "gingiva", 
                "pending_for_approval", "clinical_instructor", "url")

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
        
        # Oral Assessment
        try:
            oral_assessment_data = validated_data.pop('oral_assessment')
            oral_assessment = instance.oral_assessment
            oral_assessment.skin = oral_assessment_data.get('skin', oral_assessment.skin)
            oral_assessment.skin_desc = oral_assessment_data.get('skin_desc', oral_assessment.skin_desc)
            oral_assessment.eyes = oral_assessment_data.get('eyes', oral_assessment.eyes)
            oral_assessment.eyes_desc = oral_assessment_data.get('eyes_desc', oral_assessment.eyes_desc)
            oral_assessment.neck = oral_assessment_data.get('neck', oral_assessment.neck)
            oral_assessment.neck_desc = oral_assessment_data.get('neck_desc', oral_assessment.neck_desc)
            oral_assessment.TMD = oral_assessment_data.get('TMD', oral_assessment.TMD)
            oral_assessment.TMD_desc = oral_assessment_data.get('TMD_desc', oral_assessment.TMD_desc)
            oral_assessment.lymph_nodes = oral_assessment_data.get('lymph_nodes', oral_assessment.lymph_nodes)
            oral_assessment.lymph_nodes_desc = oral_assessment_data.get('lymph_nodes_desc', oral_assessment.lymph_nodes_desc)
            oral_assessment.lips = oral_assessment_data.get('lips', oral_assessment.lips)
            oral_assessment.lips_desc = oral_assessment_data.get('lips_desc', oral_assessment.lips_desc)
            oral_assessment.buccal_mucosa = oral_assessment_data.get('buccal_mucosa', oral_assessment.buccal_mucosa)
            oral_assessment.buccal_mucosa_desc = oral_assessment_data.get('buccal_mucosa_desc', oral_assessment.buccal_mucosa_desc)
            oral_assessment.vestibule = oral_assessment_data.get('vestibule', oral_assessment.vestibule)
            oral_assessment.vestibule_desc = oral_assessment_data.get('vestibule_desc', oral_assessment.vestibule_desc)
            oral_assessment.alveolar_ridge = oral_assessment_data.get('alveolar_ridge', oral_assessment.alveolar_ridge)
            oral_assessment.alveolar_ridge_desc = oral_assessment_data.get('alveolar_ridge_desc', oral_assessment.alveolar_ridge_desc)
            oral_assessment.hard_palate = oral_assessment_data.get('hard_palate', oral_assessment.hard_palate)
            oral_assessment.hard_palate_desc = oral_assessment_data.get('hard_palate_desc', oral_assessment.hard_palate_desc)
            oral_assessment.oro_pharynx = oral_assessment_data.get('oro_pharynx', oral_assessment.oro_pharynx)
            oral_assessment.oro_pharynx_desc = oral_assessment_data.get('oro_pharynx_desc', oral_assessment.oro_pharynx_desc)
            oral_assessment.tongue = oral_assessment_data.get('tongue', oral_assessment.tongue)
            oral_assessment.tongue_desc = oral_assessment_data.get('tongue_desc', oral_assessment.tongue_desc)
            oral_assessment.mouth_floor = oral_assessment_data.get('mouth_floor', oral_assessment.mouth_floor)
            oral_assessment.mouth_floor_desc = oral_assessment_data.get('mouth_floor_desc', oral_assessment.mouth_floor_desc)
            oral_assessment.salivary_glands = oral_assessment_data.get('salivary_glands', oral_assessment.salivary_glands)
            oral_assessment.salivary_glands_desc = oral_assessment_data.get('salivary_glands_desc', oral_assessment.salivary_glands_desc)
            oral_assessment.datetime_added = oral_assessment_data.get('datetime_added', oral_assessment.datetime_added)

            oral_assessment.save()
        except:
            pass
        
        # Occlusion
        try:
            occlusion_data = validated_data.pop('occlusion')
            occlusion = instance.occlusion
            occlusion.occlusion_class = occlusion_data.get('occlusion_class', occlusion.occlusion_class)
            occlusion.other_occlusal = occlusion_data.get('other_occlusal', occlusion.other_occlusal)
            occlusion.oral_habits = occlusion_data.get('oral_habits', occlusion.oral_habits)
            occlusion.plaque = occlusion_data.get('plaque', occlusion.plaque)
            occlusion.generalized = occlusion_data.get('generalized', occlusion.generalized)
            occlusion.localized = occlusion_data.get('localized', occlusion.localized)
            occlusion.generalized_desc = occlusion_data.get('generalized_desc', occlusion.generalized_desc)
            occlusion.localized_desc = occlusion_data.get('localized_desc', occlusion.localized_desc)
            occlusion.erosion = occlusion_data.get('erosion', occlusion.erosion)
            occlusion.demineralization = occlusion_data.get('demineralization', occlusion.demineralization)
            occlusion.attrition = occlusion_data.get('attrition', occlusion.attrition)
            occlusion.abfraction = occlusion_data.get('abfraction', occlusion.abfraction)
            occlusion.fluorosis = occlusion_data.get('fluorosis', occlusion.fluorosis)
            occlusion.abrasion = occlusion_data.get('abrasion', occlusion.abrasion)

            occlusion.save()
        except:
            pass

        # Social History

        try:
            social_history_data = validated_data.pop('social_history')
            social_history = instance.social_history
            social_history.using_tobacco = social_history_data.get('using_tobacco', social_history.using_tobacco)
            social_history.using_cigarettes = social_history_data.get('using_cigarettes', social_history.using_cigarettes)
            social_history.using_vape = social_history_data.get('using_vape', social_history.using_vape)
            social_history.using_recreation = social_history_data.get('using_recreation', social_history.using_recreation)
            social_history.using_therapeutic = social_history_data.get('using_therapeutic', social_history.using_therapeutic)
            social_history.drink_alcoholic = social_history_data.get('drink_alcoholic', social_history.drink_alcoholic)
            social_history.kind_tobacco = social_history_data.get('kind_tobacco', social_history.kind_tobacco)
            social_history.often_tobacco = social_history_data.get('often_tobacco', social_history.often_tobacco)
            social_history.years_tobacco = social_history_data.get('years_tobacco', social_history.years_tobacco)
            social_history.stop_tobacco = social_history_data.get('stop_tobacco', social_history.stop_tobacco)
            social_history.kind_cigarettes = social_history_data.get('kind_cigarettes', social_history.kind_cigarettes)
            social_history.often_cigarettes = social_history_data.get('often_cigarettes', social_history.often_cigarettes)
            social_history.years_cigarettes = social_history_data.get('years_cigarettes', social_history.years_cigarettes)
            social_history.stop_cigarettes = social_history_data.get('stop_cigarettes', social_history.stop_cigarettes)
            social_history.kind_vape = social_history_data.get('kind_vape', social_history.kind_vape)
            social_history.often_vape = social_history_data.get('often_vape', social_history.often_vape)
            social_history.years_vape = social_history_data.get('years_vape', social_history.years_vape)
            social_history.stop_vape = social_history_data.get('stop_vape', social_history.stop_vape)
            social_history.kind_recreation = social_history_data.get('kind_recreation', social_history.kind_recreation)
            social_history.often_recreation = social_history_data.get('often_recreation', social_history.often_recreation)
            social_history.years_recreation = social_history_data.get('years_recreation', social_history.years_recreation)
            social_history.stop_recreation = social_history_data.get('stop_recreation', social_history.stop_recreation)
            social_history.kind_therapeutic = social_history_data.get('kind_therapeutic', social_history.kind_therapeutic)
            social_history.often_therapeutic = social_history_data.get('often_therapeutic', social_history.often_therapeutic)
            social_history.years_therapeutic = social_history_data.get('years_therapeutic', social_history.years_therapeutic)
            social_history.stop_therapeutic = social_history_data.get('stop_therapeutic', social_history.stop_therapeutic)
            social_history.kind_alcoholic = social_history_data.get('kind_alcoholic', social_history.kind_alcoholic)
            social_history.often_alcoholic = social_history_data.get('often_alcoholic', social_history.often_alcoholic)
            social_history.years_alcoholic = social_history_data.get('years_alcoholic', social_history.years_alcoholic)
            social_history.stop_alcoholic = social_history_data.get('stop_alcoholic', social_history.stop_alcoholic)

            social_history.save()

        except:
            pass

        # Dental History
        try:
            dental_history_data = validated_data.pop('dental_history')
            dental_history = instance.dental_history
            dental_history.date_last_visit = dental_history_data.get('date_last_visit', dental_history.date_last_visit)
            dental_history.freq_dental_visit = dental_history_data.get('freq_dental_visit', dental_history.freq_dental_visit)
            dental_history.proc_last_visit = dental_history_data.get('proc_last_visit', dental_history.proc_last_visit)
            dental_history.exposure_anesthesia = dental_history_data.get('exposure_anesthesia', dental_history.exposure_anesthesia)
            dental_history.complications_dental = dental_history_data.get('complications_dental', dental_history.complications_dental)
            dental_history.brush = dental_history_data.get('brush', dental_history.brush)
            dental_history.floss = dental_history_data.get('floss', dental_history.floss)
            dental_history.rinse = dental_history_data.get('rinse', dental_history.rinse)
            dental_history.smile = dental_history_data.get('smile', dental_history.smile)
            dental_history.relevant_smile = dental_history_data.get('relevant_smile', dental_history.relevant_smile)
            dental_history.gums = dental_history_data.get('gums', dental_history.gums)
            dental_history.relevant_gums = dental_history_data.get('relevant_gums', dental_history.relevant_gums)
            dental_history.extraction = dental_history_data.get('extraction', dental_history.extraction)
            dental_history.relevant_extraction = dental_history_data.get('relevant_extraction', dental_history.relevant_extraction)
            dental_history.bled = dental_history_data.get('bled', dental_history.bled)
            dental_history.relevant_bled = dental_history_data.get('relevant_bled', dental_history.relevant_bled)
            dental_history.orthodomic = dental_history_data.get('orthodomic', dental_history.orthodomic)
            dental_history.relevant_orthodomic = dental_history_data.get('relevant_orthodomic', dental_history.relevant_orthodomic)
            dental_history.cold = dental_history_data.get('cold', dental_history.cold)
            dental_history.relevant_cold = dental_history_data.get('relevant_cold', dental_history.relevant_cold)
            dental_history.periodental = dental_history_data.get('periodental', dental_history.periodental)
            dental_history.relevant_periodental = dental_history_data.get('relevant_periodental', dental_history.relevant_periodental)
            dental_history.bleed = dental_history_data.get('bleed', dental_history.bleed)
            dental_history.relevant_bleed = dental_history_data.get('relevant_bleed', dental_history.relevant_bleed)
            dental_history.denture = dental_history_data.get('denture', dental_history.denture)
            dental_history.relevant_denture = dental_history_data.get('relevant_denture', dental_history.relevant_denture)
            dental_history.jaw_pain = dental_history_data.get('jaw_pain', dental_history.jaw_pain)
            dental_history.relevant_jaw_pain = dental_history_data.get('relevant_jaw_pain', dental_history.relevant_jaw_pain)
            dental_history.catch = dental_history_data.get('catch', dental_history.catch)
            dental_history.relevant_catch = dental_history_data.get('relevant_catch', dental_history.relevant_catch)
            dental_history.datetime_added = dental_history_data.get('datetime_added', dental_history.datetime_added)

            dental_history.save()

        except:
            pass

        # Gingiva
        try:
            gingiva_data = validated_data.pop('gingiva')
            gingiva = instance.gingiva
            gingiva.attached_gingiva = gingiva_data.get('attached_gingiva', gingiva.attached_gingiva)
            gingiva.frenular_attachment = gingiva_data.get('frenular_attachment', gingiva.frenular_attachment)
            gingiva.radiographic_stage = gingiva_data.get('radiographic_stage', gingiva.radiographic_stage)
            gingiva.radiographic_hv = gingiva_data.get('radiographic_hv', gingiva.radiographic_hv)
            gingiva.radiographic_gl = gingiva_data.get('radiographic_gl', gingiva.radiographic_gl)
            gingiva.color = gingiva_data.get('color', gingiva.color)
            gingiva.consistency = gingiva_data.get('consistency', gingiva.consistency)
            gingiva.contour = gingiva_data.get('contour', gingiva.contour)
            gingiva.texture = gingiva_data.get('texture', gingiva.texture)

            gingiva.save()

        except:
            pass

        return instance

class MixTreatmentRecordSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(required=False)
    clinician = ClinicianSerializer(required=False)
    clinical_instructor = ClinicalInstructorSerializer(required=False)
    track_record = TrackRecordSerializer(required=False)

    class Meta:
        model = TreatmentRecord
        fields = ("patient", "clinician", "clinical_instructor",  
                "track_record", "procedure", "date", "patient_signature", "instructor_signature", "id")

class MixCDARSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(required=False)
    clinician = ClinicianSerializer(required=False)
    clinical_instructor = ClinicalInstructorSerializer(required=False)
    track_record = TrackRecordSerializer(required=False)

    class Meta:
        model = CDAR
        fields = ("patient", "clinician", "clinical_instructor",  
                "track_record", "procedure", "date", "patient_signature", "instructor_signature", "id")