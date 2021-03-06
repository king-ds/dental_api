from django.db import models
from authentication.models import *

class AdditionalPersonalData(models.Model):
    chief_complaint = models.TextField()
    history_of_present_illness = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class MedicalHistory(models.Model):
    physician_care = models.BooleanField(default=False)
    hospitalization = models.TextField()
    allergies = models.CharField(max_length=255)
    illnesses = models.CharField(max_length=255)
    medications = models.TextField()
    childhood_disease_history = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class MedicalHealthQuestionnaire(models.Model):
    high_blood_pressure = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    osteoporosis = models.BooleanField(default=False)
    herpes = models.BooleanField(default=False)
    radiation_treatments = models.BooleanField(default=False)
    chemotherapy = models.BooleanField(default=False)
    artificial_heart_valves = models.BooleanField(default=False)
    heart_attack = models.BooleanField(default=False)
    pacemaker = models.BooleanField(default=False)
    angioplasty = models.BooleanField(default=False)
    stroke = models.BooleanField(default=False)
    angina_pectrosis = models.BooleanField(default=False)
    frequent_high_fever = models.BooleanField(default=False)
    sinusitis = models.BooleanField(default=False)
    empyema = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    breathing_problems = models.BooleanField(default=False)
    afternoon_fever = models.BooleanField(default=False)
    chronic_cough = models.BooleanField(default=False)
    bloody_sputum = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    frequent_heartaches = models.BooleanField(default=False)
    visual_impairment = models.BooleanField(default=False)
    hearing_impairment = models.BooleanField(default=False)
    athritis = models.BooleanField(default=False)
    pain_in_joints = models.BooleanField(default=False)
    tumors = models.BooleanField(default=False)
    swollen_ankles = models.BooleanField(default=False)
    goiter = models.BooleanField(default=False)
    frequent_thirst = models.BooleanField(default=False)
    frequent_hunger = models.BooleanField(default=False)
    frequent_urination = models.BooleanField(default=False)
    sudden_weight_loss = models.BooleanField(default=False)
    abdominal_discomfort = models.BooleanField(default=False)
    acidic_reflux = models.BooleanField(default=False)
    bleeding_bruining_easily = models.BooleanField(default=False)
    recreational_drugs = models.BooleanField(default=False)
    steroid_therapy = models.BooleanField(default=False)
    blood = models.BooleanField(default=False)
    pain_upon_urination = models.BooleanField(default=False)
    kidney_liver_problems = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    sexually_transmitted_disease = models.BooleanField(default=False)
    hiv_positive = models.BooleanField(default=False)
    fainting_spells = models.BooleanField(default=False)
    depression = models.BooleanField(default=False)
    others = models.CharField(max_length=100)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Allergy(models.Model):
    aspirin = models.BooleanField(default=False)
    penicillin = models.BooleanField(default=False)
    latex = models.BooleanField(default=False)
    metal = models.BooleanField(default=False)
    none = models.BooleanField(default=False)
    others = models.CharField(max_length=100)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Female(models.Model):
    is_pregnant = models.BooleanField(default=False)
    is_breast_feeding = models.BooleanField(default=False)
    is_menopause = models.BooleanField(default=False)
    is_under_hormone = models.BooleanField(default=False)
    pregnant = models.IntegerField(null=True)
    breast_feeding = models.IntegerField(null=True)
    menopause = models.IntegerField(null=True)
    under_hormone = models.IntegerField(null=True)
    datetime_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class SocialHistory(models.Model):
    using_tobacco = models.BooleanField(default=False)
    using_cigarettes = models.BooleanField(default=False)
    using_vape = models.BooleanField(default=False)
    using_recreation = models.BooleanField(default=False)
    using_therapeutic = models.BooleanField(default=False)
    drink_alcoholic = models.BooleanField(default=False)
    kind_tobacco = models.CharField(max_length=100)
    often_tobacco = models.CharField(max_length=100)
    years_tobacco = models.CharField(max_length=100)
    stop_tobacco = models.CharField(max_length=100)
    kind_cigarettes = models.CharField(max_length=100)
    often_cigarettes = models.CharField(max_length=100)
    years_cigarettes = models.CharField(max_length=100)
    stop_cigarettes = models.CharField(max_length=100)
    kind_vape = models.CharField(max_length=100)
    often_vape = models.CharField(max_length=100)
    years_vape = models.CharField(max_length=100)
    stop_vape = models.CharField(max_length=100)
    kind_recreation = models.CharField(max_length=100)
    often_recreation = models.CharField(max_length=100)
    years_recreation = models.CharField(max_length=100)
    stop_recreation = models.CharField(max_length=100)
    kind_therapeutic = models.CharField(max_length=100)
    often_therapeutic = models.CharField(max_length=100)
    years_therapeutic = models.CharField(max_length=100)
    stop_therapeutic = models.CharField(max_length=100)
    kind_alcoholic = models.CharField(max_length=100)
    often_alcoholic = models.CharField(max_length=100)
    years_alcoholic = models.CharField(max_length=100)
    stop_alcoholic = models.CharField(max_length=100)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class DentalHistory(models.Model):
    date_last_visit = models.DateField(null=True, blank=True)
    freq_dental_visit = models.CharField(max_length=100)
    proc_last_visit = models.CharField(max_length=100)
    exposure_anesthesia = models.CharField(max_length=100)
    complications_dental = models.CharField(max_length=100)
    brush = models.IntegerField(null=True, blank=True)
    floss = models.IntegerField(null=True, blank=True)
    rinse = models.IntegerField(null=True, blank=True)
    smile = models.BooleanField(default=False)
    relevant_smile = models.CharField(max_length=50)
    gums = models.BooleanField(default=False)
    relevant_gums = models.CharField(max_length=50)
    extraction = models.BooleanField(default=False)
    relevant_extraction = models.CharField(max_length=50)
    bled = models.BooleanField(default=False)
    relevant_bled = models.CharField(max_length=50)
    orthodomic = models.BooleanField(default=False)
    relevant_orthodomic = models.CharField(max_length=50)
    cold = models.BooleanField(default=False)
    relevant_cold = models.CharField(max_length=50)
    periodental = models.BooleanField(default=False)
    relevant_periodental = models.CharField(max_length=50)
    bleed = models.BooleanField(default=False)
    relevant_bleed = models.CharField(max_length=50)
    denture = models.BooleanField(default=False)
    relevant_denture = models.CharField(max_length=50)
    jaw_pain = models.BooleanField(default=False)
    relevant_jaw_pain = models.CharField(max_length=50)
    catch = models.BooleanField(default=False)
    relevant_catch = models.CharField(max_length=50)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class OralAssessment(models.Model):
    skin = models.BooleanField(default=False)
    skin_desc = models.CharField(max_length=200)
    eyes = models.BooleanField(default=False)
    eyes_desc = models.CharField(max_length=200)
    neck = models.BooleanField(default=False)
    neck_desc = models.CharField(max_length=200)
    TMD = models.BooleanField(default=False)
    TMD_desc = models.CharField(max_length=200)
    lymph_nodes = models.BooleanField(default=False)
    lymph_nodes_desc = models.CharField(max_length=200)
    lips = models.BooleanField(default=False)
    lips_desc = models.CharField(max_length=200)
    buccal_mucosa = models.BooleanField(default=False)
    buccal_mucosa_desc = models.CharField(max_length=200)
    vestibule = models.BooleanField(default=False)
    vestibule_desc = models.CharField(max_length=200)
    alveolar_ridge = models.BooleanField(default=False)
    alveolar_ridge_desc = models.CharField(max_length=200)
    hard_palate = models.BooleanField(default=False)
    hard_palate_desc = models.CharField(max_length=200)
    oro_pharynx = models.BooleanField(default=False)
    oro_pharynx_desc = models.CharField(max_length=200)
    tongue = models.BooleanField(default=False)
    tongue_desc = models.CharField(max_length=200)
    mouth_floor = models.BooleanField(default=False)
    mouth_floor_desc = models.CharField(max_length=200)
    salivary_glands = models.BooleanField(default=False)
    salivary_glands_desc = models.CharField(max_length=200)
    datetime_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class Occlusion(models.Model):
    occlusion_class = models.CharField(max_length=20)
    other_occlusal = models.CharField(max_length=200)
    oral_habits = models.CharField(max_length=200)
    plaque = models.CharField(max_length=20)
    generalized = models.BooleanField(default=False)
    localized = models.BooleanField(default=False)
    generalized_desc = models.CharField(max_length=50)
    localized_desc = models.CharField(max_length=50)
    erosion = models.BooleanField(default=False)
    demineralization = models.BooleanField(default=False)
    attrition = models.BooleanField(default=False)
    abfraction = models.BooleanField(default=False)
    fluorosis = models.BooleanField(default=False)
    abrasion = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Gingiva(models.Model):
    attached_gingiva = models.CharField(max_length=10)
    frenular_attachment = models.CharField(max_length=10)
    radiographic_stage = models.CharField(max_length=20)
    radiographic_hv = models.CharField(max_length=20)
    radiographic_gl = models.CharField(max_length=20)
    color = models.CharField(max_length=200)
    consistency = models.CharField(max_length=200)
    contour = models.CharField(max_length=200)
    texture = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class PeriodontalDiagnosis(models.Model):
    asa_type = models.CharField(max_length=20)
    aap_classification = models.TextField()
    medical_concerns = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class TrackRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE, blank=True, null=True)
    clinical_instructor = models.ForeignKey(ClinicalInstructor, on_delete=models.CASCADE, blank=True, null=True)
    additional_personal_data = models.ForeignKey(AdditionalPersonalData, on_delete=models.CASCADE, blank=True, null=True)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, blank=True, null=True)
    medical_health_questionnaire = models.ForeignKey(MedicalHealthQuestionnaire, on_delete=models.CASCADE, blank=True, null=True)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE, blank=True, null=True)
    female = models.ForeignKey(Female, on_delete=models.CASCADE, blank=True, null=True)
    social_history = models.ForeignKey(SocialHistory, on_delete=models.CASCADE, blank=True, null=True)
    dental_history = models.ForeignKey(DentalHistory, on_delete=models.CASCADE, blank=True, null=True)
    oral_assessment = models.ForeignKey(OralAssessment, on_delete=models.CASCADE, blank=True, null=True)
    occlusion = models.ForeignKey(Occlusion, on_delete=models.CASCADE, blank=True, null=True)
    gingiva = models.ForeignKey(Gingiva, on_delete=models.CASCADE, blank=True, null=True)
    pending_for_approval = models.BooleanField(default=False)
    is_approved_instructor = models.BooleanField(default=False)
    is_approved_patient = models.BooleanField(default=False)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class VitalSign(models.Model):
    BP_1 = models.IntegerField(null=True)
    BP_2 = models.IntegerField(null=True)
    PR = models.FloatField(null=True)
    RR = models.FloatField(null=True)
    TEMP = models.FloatField(null=True)
    datetime_taken = models.DateTimeField(auto_now_add=True)
    track_record = models.ForeignKey(TrackRecord, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Diagnosis(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    track_record = models.ForeignKey(TrackRecord, on_delete=models.CASCADE, blank=True, null=True)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class TreatmentPlan(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    track_record = models.ForeignKey(TrackRecord, on_delete=models.CASCADE, blank=True, null=True)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class TreatmentRecord(models.Model):
    date = models.DateField(null=True, blank=True)
    procedure = models.CharField(max_length=100)
    treatment_notes = models.TextField()
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE, blank=True, null=True)
    clinical_instructor = models.ForeignKey(ClinicalInstructor, on_delete=models.CASCADE, blank=True, null=True)
    patient_signature = models.BooleanField(default=False)
    instructor_signature = models.BooleanField(default=False)
    track_record = models.ForeignKey(TrackRecord, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.track_record)

class CDAR(models.Model):
    date = models.DateField(null=True, blank=True)
    procedure = models.CharField(max_length=100)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE, blank=True, null=True)
    clinical_instructor = models.ForeignKey(ClinicalInstructor, on_delete=models.CASCADE, blank=True, null=True)
    patient_signature = models.BooleanField(default=False)
    instructor_signature = models.BooleanField(default=False)
    pending_for_approval = models.BooleanField(default=False)
    from_treatment_record = models.BooleanField(default=False)
    treatment_record = models.IntegerField(null=False)
    track_record = models.ForeignKey(TrackRecord, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.track_record)

class DentalChart(models.Model):
    teeth_number = models.IntegerField(null=True)
    kind = models.CharField(max_length=10)
    quadrant = models.IntegerField(null=True)
    CF = models.BooleanField(default=False)
    Ab = models.BooleanField(default=False)
    Am = models.BooleanField(default=False)
    APC = models.BooleanField(default=False)
    C = models.BooleanField(default=False)
    Co = models.BooleanField(default=False)
    CD = models.BooleanField(default=False)
    GC = models.BooleanField(default=False)
    GI = models.BooleanField(default=False)
    Imp = models.BooleanField(default=False)
    In = models.BooleanField(default=False)
    M = models.BooleanField(default=False)
    MC = models.BooleanField(default=False)
    P = models.BooleanField(default=False)
    PFG = models.BooleanField(default=False)
    F = models.BooleanField(default=False)
    PFM = models.BooleanField(default=False)
    PFS = models.BooleanField(default=False)
    RC = models.BooleanField(default=False)
    RPD = models.BooleanField(default=False)
    SS = models.BooleanField(default=False)
    Un = models.BooleanField(default=False)
    X = models.BooleanField(default=False)
    top = models.CharField(max_length=20) # r = red, b = blue, rb = red,blue
    left = models.CharField(max_length=20)
    right = models.CharField(max_length=20)
    bottom = models.CharField(max_length=20)
    middle = models.CharField(max_length=20)
    track_record = models.ForeignKey(TrackRecord, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.track_record)