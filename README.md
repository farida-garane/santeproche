#  SantéProche

### 📌 Description

**SantéProche** est une application web développée avec **Django** qui permet aux patients de trouver un centre de santé disponible à proximité et de centraliser leur historique médical. Elle fournit une interface simple pour :

* S'enregistrer et se connecter selon son rôle (patient, soignant, gérant de centre)
* Consulter la liste des centres de santé (CSPS, cliniques, pharmacies, hôpitaux) avec leur statut
* Centraliser son carnet de santé numérique, peu importe le centre visité
* Créer des dossiers médicaux (consultations, diagnostics, traitements) en tant que soignant
* Gérer son propre centre de santé en tant que gérant

---

### 📂 Structure du projet

```
santeproche/
├── venv/                        # Environnement virtuel Python
├── santeproche_config/           # Configuration globale du projet
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/                     # Utilisateurs, rôles, authentification
│   ├── models.py                 # User custom (patient/soignant/centre)
│   ├── views.py
│   ├── forms.py
│   ├── decorators.py             # Permissions par rôle
│   └── templates/accounts/
├── centers/                      # Centres de santé
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/centers/
├── records/                      # Dossiers médicaux
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/records/
├── templates/                    # Templates globaux (base.html, accueil.html)
├── .env                         # Variables d'environnement (non versionné)
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

### ⚙️ Installation et configuration

#### 1. Cloner le dépôt

```bash
git clone <url-du-repo>
cd santeproche
```

#### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate       # Linux/macOS/WSL
venv\Scripts\activate          # Windows
```

#### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

#### 4. Configurer les variables d'environnement

Créer un fichier `.env` à la racine :

```env
DB_NAME=santeproche_db
DB_USER=postgres
DB_PASSWORD=ton_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

#### 5. Créer la base de données PostgreSQL

```bash
sudo -u postgres psql
CREATE DATABASE santeproche_db;
\q
```

#### 6. Appliquer les migrations

```bash
python manage.py migrate
```

#### 7. Créer un compte administrateur

```bash
python manage.py createsuperuser
```

---

### 🚀 Lancer l'application

```bash
python manage.py runserver
```

Accède à [http://127.0.0.1:8000](http://127.0.0.1:8000) dans ton navigateur.

---

### 🌟 Fonctionnalités principales

#### 🔐 Authentification et rôles
- Inscription avec choix du rôle (patient, soignant, gérant de centre)
- Connexion et déconnexion sécurisées
- Permissions par rôle sur chaque page (décorateurs custom)

#### 🏥 Centres de santé
- Liste et recherche des centres de santé
- Détail d'un centre (adresse, horaires, statut ouvert/fermé)
- Création et gestion du centre par son gérant

#### 📋 Dossiers médicaux
- Carnet de santé centralisé par patient, peu importe le centre visité
- Création de consultations par les soignants (symptômes, diagnostic, traitement)
- Consultation de l'historique par le patient concerné

---

### 🗄️ Base de données

#### Modèles principaux

**User** (`accounts`)
- Authentification standard Django (username, email, mot de passe)
- Champ `role` (patient / soignant / centre) et `telephone`

**HealthCenter** (`centers`)
- Nom, type (CSPS, clinique, pharmacie, hôpital), adresse, ville
- Statut ouvert/fermé, horaires
- Lien vers le `User` gérant

**MedicalRecord** (`records`)
- Lien vers le patient et le soignant concernés
- Lien vers le centre de santé
- Symptômes, diagnostic, traitement, date de consultation

---

### 📘 Technologies et bibliothèques utilisées

#### Backend & Frontend
- **[Django](https://www.djangoproject.com/)** - Framework web Python (architecture MVT, rendu côté serveur)
- **[python-decouple](https://pypi.org/project/python-decouple/)** - Gestion des variables d'environnement

#### Base de données
- **[PostgreSQL](https://www.postgresql.org/)** - Base de données relationnelle
- **[psycopg2](https://pypi.org/project/psycopg2/)** - Connecteur PostgreSQL pour Python

#### Frontend
- **Django Template Language (DTL)** - Moteur de templates intégré à Django

---

### ✅ Roadmap et améliorations futures

#### 🎯 Priorité haute
- [ ] Prise de rendez-vous en ligne
- [ ] Gestion des stocks de médicaments (pharmacies)
- [ ] Notifications (nouveau diagnostic, rappel de traitement)

#### 🔧 Améliorations techniques
- [ ] Tests automatisés (unittest/pytest)
- [ ] Recherche avancée avec filtres (ville, type, disponibilité)
- [ ] Déploiement en production (Render/Railway)

#### 🎨 UX/UI
- [ ] Feuille de style CSS globale
- [ ] Dashboard personnalisé par rôle
- [ ] Interface responsive mobile

#### 🛡️ Sécurité
- [ ] Restriction stricte de l'accès aux dossiers médicaux (patient/soignant concernés uniquement)
- [ ] Validation renforcée des formulaires
- [ ] HTTPS obligatoire en production

---

### 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Crée une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit tes changements (`git commit -am 'Ajoute nouvelle fonctionnalité'`)
4. Push sur la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvre une Pull Request

---

### 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

### 👩‍💻 Auteure

Développé par **Farida Anne Kevine Garané** 

---

*Dernière mise à jour : Août 2026*
