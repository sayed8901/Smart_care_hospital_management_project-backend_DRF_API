from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime


APPOINTMENT_TYPES = [
    ('Online','Online'),
    ('Offline','Offline'),
]

APPOINTMENT_STATUS = [
    ('Pending','Pending'),
    ('Running','Running'),
    ('Completed','Completed'),
]


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor", on_delete=models.CASCADE)

    appointment_types = models.CharField(choices=APPOINTMENT_TYPES, max_length=10)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=10, default="Pending")

    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE, related_name='available_time')

    symptom = models.TextField()
    cancel = models.BooleanField(default=False)


    def __str__(self):
        return f"Patient: '{self.patient.user.first_name}' booked an appointment to Doctor: '{self.doctor.user.first_name}'"
