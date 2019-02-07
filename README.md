Users APP
=======

A Complete Django Application with Custom User Model, Custom Authentication Middleware, Auto Generated Fields in the User Model that will be generated automatically on the save method call

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed.
2.  Clone the repo and configure the virtualenv: For beginners virtualenv ('django_env') is already available in repo, so activate it.

```
$ git clone https://github.com/asadmanzoor93/users-app.git
$ cd users-app
$ source django_env/bin/activate
```

3.  Set up the initial migration for our custom user models in `users` and build the database.

```
(users-app) $ python manage.py makemigrations users
(users-app) $ python manage.py migrate
```

4.  Create a superuser:

```
(users-app) $ python manage.py createsuperuser
```

5.  Confirm everything is working:

```
(users-app) $ python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).
