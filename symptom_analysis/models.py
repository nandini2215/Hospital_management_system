from django.db import models

# Doctor model
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Patient model with assigned doctor
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')
    
    def __str__(self):
        return self.name

# Symptom model
class Symptom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    severity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

# Disease model connected to symptoms
class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    symptoms = models.ManyToManyField(Symptom, related_name='diseases')

    def __str__(self):
        return self.name

# Medication model linked to disease
class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} for {self.disease.name}"

# Diet model linked to disease
class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='diets')
    recommendation = models.TextField()

    def __str__(self):
        return f"Diet for {self.disease.name}"

# Precaution model linked to disease
class Precaution(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='precautions')
    advice = models.CharField(max_length=200)

    def __str__(self):
        return f"Precaution for {self.disease.name}"

# Workout model linked to disease
class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='workouts')
    routine = models.TextField()

    def __str__(self):
        return f"Workout for {self.disease.name}"

# PatientHistory model
class PatientHistory(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='history')
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='patient_histories')
    symptoms = models.ManyToManyField(Symptom, related_name='patient_histories')
    diagnosis_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient.name} - {self.disease.name} ({self.diagnosis_date})"
