# Boilerplate Django
This code allows the setup of a fully functionnal Django server supporting:

* classic HTTP route requests (Django core)
* REST API (through Django Rest Framework)
* Websockets (through Django channels)

## Quickstart

> Requirements:
> 
> You need Python 3.4 or more 

1. Install pipenv :
    ```bash
    pip install --upgrade pip
    pip install pipenv
    ```
1. Clone project
1. Open a term within  the `boilerplate_django` folder and install/start the virtual env:
    ```shell
    # Building/starting the virtual env
    pipenv install
    pipenv shell
    
    # Creating/updating the database according to your apps models
    manage.py makemigrations   # prefix with "python " if you're encoutering python PATH issues
    manage.py migrate          # prefix with "python " if you're encoutering python PATH issues
    
    # Run the Django server
    manage.py runserver
    ```
1. Access your app at [http://localhost:8000](http://localhost:8000)
1. Access you backoffice at [http://localhost:8000/admin](http://localhost:8000/admin)

## Backoffice
You can access your backoffice thanks to the un believable admin/admin login and password.