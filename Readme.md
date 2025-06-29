# BanaoTask1

A Django-based web application with custom user authentication for patients and doctors.

## Features

- Custom user model with profile picture and address fields
- Separate dashboards for patients and doctors
- User registration and login/logout functionality
- Media upload support for profile pictures

## Project Structure

```
banaoTask1/
    manage.py
    db.sqlite3
    banaoTask1/
        settings.py
        urls.py
        ...
    accounts/
        models.py
        views.py
        forms.py
        urls.py
        templates/
    media/
    static/
```

## Setup Instructions

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies** (preferably in a virtual environment):

    ```sh
    pip install django
    ```

3. **Apply migrations**:

    ```sh
    python manage.py migrate
    ```

4. **Create a superuser** (optional, for admin access):

    ```sh
    python manage.py createsuperuser
    ```

5. **Run the development server**:

    ```sh
    python manage.py runserver
    ```

6. **Access the app**:

    - Visit `http://127.0.0.1:8000/accounts/signup/` to register.
    - Visit `http://127.0.0.1:8000/accounts/login/` to log in.

## Notes

- Uploaded profile pictures are stored in the `media/profiles/` directory.
- Static files are served from the `static/` directory during development.
S