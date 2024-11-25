
# Netfix

Netfix est une plateforme web permettant aux utilisateurs de s'inscrire, de choisir et de payer des services proposés par différentes entreprises. Ce projet est développé avec le framework Django.

## Objectifs du projet

Netfix vise à simplifier l'accès à divers services tels que :
- Réparation d'équipements ménagers
- Peinture
- Nettoyage
- Et bien plus encore.

Le projet est en cours de développement et certaines fonctionnalités restent à implémenter.

## Fonctionnalités

- **Types d'utilisateurs :**
  - **Client** : peut rechercher, consulter et demander des services.
  - **Entreprise** : peut créer et proposer des services dans des catégories spécifiques.
  
- **Inscription et connexion :**
  - Les utilisateurs doivent fournir une adresse e-mail unique et un mot de passe.
  - Les champs requis pour l'inscription :
    - **Client** : Email, mot de passe, nom d'utilisateur, date de naissance.
    - **Entreprise** : Email, mot de passe, nom d'utilisateur, domaine d'activité.

- **Profils personnalisés :**
  - Les clients voient leurs demandes de service précédentes.
  - Les entreprises affichent leurs services proposés.

- **Services :**
  - Chaque service inclut un nom, une description, un prix par heure, et une date de création.
  - Les entreprises peuvent proposer des services uniquement dans leur domaine d'activité.

- **Pages dédiées :**
  - Liste des services par catégorie.
  - Page détaillée pour chaque service.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://zone01normandie.org/git/draftandj/netfix.git
   cd netfix
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Appliquez les migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

## Structure du projet

- **Applications Django :**
  - `users` : Gestion des utilisateurs (inscription, connexion, profils).
  - `services` : Gestion des services (création, affichage, demande).
  - `main` : Fonctionnalités globales (page d'accueil, navigation).

## Bonus

Pour améliorer le projet :
- Implémentez un système de notation pour les services.
- Ajoutez des filtres pour faciliter la recherche des services.

## Technologies utilisées

- **Backend** : Python, Django (v3.1.14)
- **Frontend** : HTML, CSS (avec des templates Django)

## Contributions

Les contributions sont les bienvenues. Si vous trouvez des problèmes, n'hésitez pas à soumettre une issue ou une pull request.

## Auteur

- Djihadi Raftandjani (raftandj)
