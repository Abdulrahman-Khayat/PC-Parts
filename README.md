# PC Parts API
## Introduction
Welcome to the PC Parts API, a Django-based project that provides information about PC components. This API allows you to access detailed information about various PC parts, including processors, graphics cards, memory modules, and more.

## Getting Started
1. Configure the application by customizing and saving the following snippet in `pc_parts/pc_parts/.env`:

    ```
    DATABASE_HOST=localhost
    DATABASE_NAME=pcparts
    DATABASE_USER=pcparts
    DATABASE_PASS=pcpartspassword
    DATABASE_PORT=5432
    ```
    
2. Run Postgres locally:

        docker run -d \
            --name postgres-container \
            -e POSTGRES_USER=pcparts \
            -e POSTGRES_PASSWORD=pcpartspassword \
            -p 5432:5432 \
            postgres

3. Install Poetry:

        pip install poetry
4. Install dependencies:

        poetry install
5. Activate virtual environment:

        poetry shell



6. Apply migrations:

         python manage.py migrate

7. To seed database:

        python manage.py loaddata categories brands --app products
8. Run the Development Server:

        python manage.py runserver
