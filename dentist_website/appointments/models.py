from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    dentist_name = models.CharField(max_length=100)
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment with {self.dentist_name} on {self.date} at {self.time}"
