from django.contrib import admin
from .models import Patient, Doctor, Disease, Symptom,Medication,Diet,Precaution,Workout,PatientHistory

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Medication)
admin.site.register(Diet)
admin.site.register(Precaution)
admin.site.register(Workout)
admin.site.register(PatientHistory)


