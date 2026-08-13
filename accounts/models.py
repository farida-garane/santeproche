
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        PATIENT = 'patient', 'Patient'
        SOIGNANT = 'soignant', 'Soignant'
        CENTRE = 'centre', 'Gérant de centre'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.PATIENT,
    )
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def is_patient(self):
        return self.role == self.Role.PATIENT

    def is_soignant(self):
        return self.role == self.Role.SOIGNANT

    def is_centre(self):
        return self.role == self.Role.CENTRE
