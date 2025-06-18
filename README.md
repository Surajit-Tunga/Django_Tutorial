# Django Tutorial

## What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It helps developers build secure, scalable, and maintainable web applications quickly.

## How Django Works:

1. **Project Setup**:  
   - Install Django with `pip install django`.
   - Start a project using `django-admin startproject projectname`.

2. **App Creation**:  
   - Inside your project, create apps (modules) using `python manage.py startapp appname`.

3. **URL Routing**:  
   - URLs are mapped to views using the `urls.py` file.
   - Example: `/home` URL calls a specific function in `views.py`.

4. **Views**:  
   - Views are Python functions/classes in `views.py` that process requests and return responses (HTML, JSON, etc.).

5. **Templates**:  
   - Use HTML templates to render dynamic content. Templates can access data passed from views.

6. **Models & Database**:  
   - Define data models (tables) in `models.py`.
   - Django auto-generates database tables and provides an ORM (Object Relational Mapper).
   - Migrate models to the database using `python manage.py makemigrations` and `python manage.py migrate`.

7. **Admin Interface**:  
   - Django offers a built-in admin panel for managing data.
   - Register models in `admin.py` to make them accessible in the admin.

8. **Run Server**:  
   - Start development server with `python manage.py runserver`.
   - Visit `http://127.0.0.1:8000/` in your browser to see your app.

## Example Workflow

1. Create project & app
2. Define models
3. Register models in admin
4. Set up views and templates
5. Map URLs to views
6. Migrate database
7. Run server and develop your website!

---

For more detailed instructions, check the [Django Documentation](https://docs.djangoproject.com/en/stable/).

---

## Video Tutorial

- [YouTube Video Tutorial](https://youtu.be/JxzZxdht-XY?si=TWNbzOZaC8w7YCXK)

---

Happy Coding! 🚀
