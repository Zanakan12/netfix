
# Plateforme de Services - Django

Une plateforme permettant aux entreprises de créer des services (peinture, plomberie, jardinage, etc.) et aux clients de les demander. Ce projet utilise le framework Django pour le backend et offre des fonctionnalités d’authentification, de gestion de profils et de services.

## Table des Matières
- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
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

### Utilisation

- Accédez à la page d’accueil et inscrivez-vous en tant que **Client** ou **Entreprise**.
- Une fois connecté, accédez à votre **profil** pour gérer vos informations.
- Les entreprises peuvent créer des services, visibles par les clients, qui peuvent en faire la demande.
- Utilisez l’interface **Admin Django** pour vérifier les utilisateurs, les services, et les demandes de service.

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
