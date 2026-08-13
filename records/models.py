
from django.db import models
from django.conf import settings
from centers.models import HealthCenter


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='dossiers_patient',
        limit_choices_to={'role': 'patient'},
    )
    soignant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='dossiers_soignant',
        limit_choices_to={'role': 'soignant'},
    )
    health_center = models.ForeignKey(HealthCenter, on_delete=models.SET_NULL, null=True)

    date_consultation = models.DateTimeField(auto_now_add=True)
    symptomes = models.TextField()
    diagnostic = models.TextField()
    traitement = models.TextField(blank=True)

    def __str__(self):
        return f"Dossier de {self.patient.username} — {self.date_consultation.strftime('%d/%m/%Y')}"