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
2. Install Poetry:

        pip install poetry
3. Install dependencies:

        poetry install
4. Activate virtual environment:

        poetry shell

5. Run Postgres locally:

        docker run -d \
            --name postgres-container \
            -e POSTGRES_USER=pcparts \
            -e POSTGRES_PASSWORD=pcpartspassword \
            -p 5432:5432 \
            postgres

6. Apply migrations:

         python manage.py migrate

7. Run the Development Server:

        python manage.py runserver