# SantéProche

Plateforme web permettant de trouver un centre de santé disponible à proximité et de centraliser son historique médical.

## Fonctionnalités

- Recherche de centres de santé (CSPS, cliniques, pharmacies)
- Carnet de santé numérique par patient
- Gestion des dossiers médicaux par les soignants
- Gestion des centres par leurs gérants

## Stack

- Django (MVT)
- PostgreSQL

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rôles

- **Patient** : consulte son carnet de santé, recherche des centres
- **Soignant** : crée des dossiers médicaux
- **Gérant de centre** : gère son centre de santé

## Licence

Ce projet est sous licence MIT.
