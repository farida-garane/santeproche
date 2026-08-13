from django.db import models
from django.conf import settings


class HealthCenter(models.Model):

    class TypeCentre(models.TextChoices):
        CSPS = 'csps', 'CSPS'
        CLINIQUE = 'clinique', 'Clinique'
        PHARMACIE = 'pharmacie', 'Pharmacie'
        HOPITAL = 'hopital', 'Hôpital'

    gerant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='centre_gere',
        limit_choices_to={'role': 'centre'},
    )
    name = models.CharField(max_length=200)
    type_centre = models.CharField(max_length=15, choices=TypeCentre.choices)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True)
    est_ouvert = models.BooleanField(default=True)
    horaires = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_centre_display()})"