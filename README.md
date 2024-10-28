# Plateforme de Services - Django

Une plateforme permettant aux entreprises de créer des services (peinture, plomberie, jardinage, etc.) et aux clients de les demander. Ce projet utilise le framework Django pour le backend et offre des fonctionnalités d’authentification, de gestion de profils et de services.

## Table des Matières
- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Méthodologie SCRUM](#méthodologie-scrum)
- [Modélisation MERISE](#modélisation-merise)
- [Structure du Projet](#structure-du-projet)
- [Commandes Utiles](#commandes-utiles)
- [Contributions](#contributions)

---

### Aperçu

Ce projet de plateforme de services permet aux entreprises de proposer leurs services et aux clients de faire des demandes. Les utilisateurs peuvent s'inscrire comme **client** ou **entreprise**, chaque type ayant des fonctionnalités spécifiques (demande de service, création de services, etc.).

### Fonctionnalités

- **Inscription et Connexion** pour les utilisateurs (Clients et Entreprises)
- **Pages de Profil** spécifiques à chaque type d’utilisateur :
  - Clients : liste des services demandés
  - Entreprises : liste des services offerts
- **Création de Services** par les entreprises selon leur domaine de travail
- **Demande de Services** par les clients avec calcul des coûts basés sur le temps et l’adresse fournie
- **Affichage des Services** par catégorie et par ordre de création

### Prérequis

- **Python 3.x**
- **Django 3.1.14**
- **Virtualenv** pour la gestion des dépendances (recommandé)

### Installation

1. **Clonez le repository** :
   ```bash
   git clone <URL-du-repository>
   cd netfix
   ```

2. **Créez un environnement virtuel** et activez-le :
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Installez les dépendances** nécessaires :
   ```bash
   pip install Django==3.1.14
   ```

4. **Configurez la base de données** et appliquez les migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créez un super utilisateur** pour accéder à l’interface admin :
   ```bash
   python manage.py createsuperuser
   ```

6. **Lancez le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

Le site sera accessible à [http://localhost:8000](http://localhost:8000).

---

### Méthodologie SCRUM

SCRUM est une méthodologie agile permettant d’organiser le développement en sprints. Voici un plan SCRUM pour le projet.

#### Rôles dans le projet

- **Product Owner (PO)** : Définit les besoins et priorise les tâches.
- **Scrum Master** : Facilite l’équipe et supervise l’application de SCRUM.
- **Équipe de développement** : Implémente les tâches en suivant le backlog.

#### Product Backlog (Liste des Fonctionnalités)

1. **US01** : Inscription client
2. **US02** : Inscription entreprise
3. **US03** : Connexion utilisateur
4. **US04** : Profil client
5. **US05** : Profil entreprise
6. **US06** : Création de service
7. **US07** : Demande de service
8. **US08** : Page de services populaires
9. **US09** : Filtrage par catégorie
10. **US10** : Interface admin

#### Découpage en Sprints

- **Sprint 1** : Authentification et inscription (US01, US02, US03)
- **Sprint 2** : Gestion des profils et services (US04, US05, US06)
- **Sprint 3** : Demande de services et pages publiques (US07 à US10)

À chaque sprint, un **Daily Standup** est recommandé pour suivre l’avancement, et chaque sprint se termine par une **Revue** et une **Rétrospective**.

---

### Modélisation MERISE

La modélisation MERISE est utilisée pour concevoir la structure de données et les relations entre les entités du projet.

#### Modèle Conceptuel des Données (MCD)

1. **Utilisateur** : `id_utilisateur`, `email`, `password`, `type_utilisateur`
2. **Client** : `id_client`, `nom`, `prenom`, `date_naissance`
3. **Entreprise** : `id_entreprise`, `nom_entreprise`, `domaine_travail`
4. **Service** : `id_service`, `nom_service`, `description`, `domaine`, `prix_par_heure`, `date_creation`
5. **Demande de Service** : `id_demande`, `adresse`, `duree_estimee`, `date_demande`, `cout_estime`

#### Modèle Logique des Données (MLD)

| Table | Attributs |
|-------|-----------|
| Utilisateur | id_utilisateur (PK), email (unique), password, type_utilisateur |
| Client | id_client (PK, FK vers Utilisateur), nom, prenom, date_naissance |
| Entreprise | id_entreprise (PK, FK vers Utilisateur), nom_entreprise, domaine_travail |
| Service | id_service (PK), id_entreprise (FK vers Entreprise), nom_service, description, domaine, prix_par_heure, date_creation |
| Demande de Service | id_demande (PK), id_client (FK vers Client), id_service (FK vers Service), adresse, duree_estimee, date_demande, cout_estime |

#### Modèle Physique des Données (MPD)

```sql
CREATE TABLE Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    type_utilisateur VARCHAR(10) CHECK (type_utilisateur IN ('Client', 'Entreprise'))
);

CREATE TABLE Client (
    id_client INTEGER PRIMARY KEY REFERENCES Utilisateur(id_utilisateur),
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE
);

CREATE TABLE Entreprise (
    id_entreprise INTEGER PRIMARY KEY REFERENCES Utilisateur(id_utilisateur),
    nom_entreprise VARCHAR(255) NOT NULL,
    domaine_travail VARCHAR(50) CHECK (domaine_travail IN ('Air Conditioner', 'Carpentry', ...))
);

CREATE TABLE Service (
    id_service SERIAL PRIMARY KEY,
    id_entreprise INTEGER REFERENCES Entreprise(id_entreprise),
    nom_service VARCHAR(255) NOT NULL,
    description TEXT,
    domaine VARCHAR(50) CHECK (domaine IN ('Air Conditioner', 'Carpentry', ...)),
    prix_par_heure DECIMAL(10, 2),
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Demande_de_Service (
    id_demande SERIAL PRIMARY KEY,
    id_client INTEGER REFERENCES Client(id_client),
    id_service INTEGER REFERENCES Service(id_service),
    adresse VARCHAR(255),
    duree_estimee INTEGER,
    date_demande TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cout_estime DECIMAL(10, 2)
);
```

### Structure du Projet

```
netfix/                     # Dossier du projet Django
├── main/                   # Application principale
│   ├── templates/
│   └── urls.py
├── services/               # Application de gestion des services
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
├── users/                  # Application de gestion des utilisateurs
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
├── static/                 # Dossier pour les fichiers statiques (CSS, JS)
├── templates/              # Dossier pour les templates généraux
└── manage.py               # Commandes de gestion du projet
```

### Commandes Utiles

- **Lancer le serveur** :
  ```bash
  python manage.py runserver
  ```

- **Appliquer les migrations** :
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Créer un super utilisateur** :
  ```bash
  python manage.py createsuperuser
  ```

### Contributions

Les contributions sont les bienvenues ! Veuillez forker ce repository, créer une branche pour vos fonctionnalités, puis soumettre une pull request. Avant de contribuer, assurez-vous de tester votre code et d'inclure des commentaires explicatifs si nécessaire.

--- 

**Merci d’utiliser cette plateforme de services !**
