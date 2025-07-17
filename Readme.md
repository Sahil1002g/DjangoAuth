# BanaoTask1

A Django-based web application with custom user authentication for patients and doctors.

## Features

- Custom user model with profile picture and address fields
- Separate dashboards for patients and doctors
- User registration and login/logout functionality
- Media upload support for profile pictures

## Blog System

- Doctors can create and manage blog posts in 4 categories: Mental Health, Heart Disease, Covid19, Immunization.
- Blog post fields: Title, Image, Category, Summary, Content, Draft status.
- Doctors see only their own posts (including drafts).
- Patients can view all published (non-draft) posts, filtered by category.
- Blog summaries are truncated to 15 words with '...' appended if longer.
- Images are uploaded and displayed with posts.

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
    blog/
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
   pip install django mysqlclient python-decouple
   ```

3. **Configure MySQL database**  
   Add your credentials to a `.env` file:

   ```
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   ```

4. **Apply migrations**:

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```sh
   python manage.py runserver
   ```

7. **Access the app**:

   - Visit `http://127.0.0.1:8000/accounts/signup/` to register.
   - Visit `http://127.0.0.1:8000/accounts/login/` to log in.
   - Visit `http://127.0.0.1:8000/blog/create/` for doctors to create blog posts.
   - Visit `http://127.0.0.1:8000/blog/category/` or `http://127.0.0.1:8000/blog/blogs/` for patients to view posts.

## Notes

- Uploaded profile pictures are stored in the `media/profiles/` directory.
- Blog images are stored in the `media/blog_images/` directory.
- Static files are served from the `static/` directory during
