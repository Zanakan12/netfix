
# Netfix

Netfix is a web platform that allows users to register, choose, and pay for services offered by various companies. This project is built using the Django framework.

## Project Objectives

Netfix aims to simplify access to various services such as:
- Appliance repair
- Painting
- Cleaning
- And much more.

The project is still under development, and some features remain to be implemented.

## Features

- **User Types:**
  - **Customer:** Can search, view, and request services.
  - **Company:** Can create and offer services in specific categories.

- **Registration and Login:**
  - Users can authenticate in two ways:
    - Via email and password (classic).
    - **Via Google authentication.**
  - Required fields for classic registration:
    - **Customer:** Email, password, username, date of birth.
    - **Company:** Email, password, username, field of work.

- **Personalized Profiles:**
  - Customers can view their previous service requests.
  - Companies display their offered services.

- **Services:**
  - Each service includes a name, description, hourly rate, and creation date.
  - Companies can only offer services in their field of work.

- **Dedicated Pages:**
  - List of services by category.
  - Detailed page for each service.

## Installation

1. Clone the repository:
   ```bash
   git clone https://zone01normandie.org/git/draftandj/netfix.git
   cd netfix
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys for Google authentication:
   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google OAuth API.
   - Create credentials for a web application and obtain a **Client ID** and **Client Secret**.
   - Add these details to the environment variables or configuration file.

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- **Django Applications:**
  - `users`: Manages user-related functionalities (registration, login, profiles, Google authentication).
  - `services`: Manages service-related functionalities (creation, display, requests).
  - `main`: Manages global features (homepage, navigation).

## Bonus Features
- - **OAuth:** Google API for authentication

## Technologies Used

- **Backend:** Python, Django (v3.1.14)
- **Frontend:** HTML, CSS (using Django templates)
- **OAuth:** Google API for authentication

## Contributions

Contributions are welcome. If you find any issues, feel free to submit an issue or a pull request.

## Author

- Djihadi Raftandjani (raftandj)
