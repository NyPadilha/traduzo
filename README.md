# :construction: CSS not Finished :construction:
# Traduzo (Trybe Project)

A text translation tool between several languages, using Python with the Flask Framework, to create a Server Side application. In other words, the Back-end (via the controller) will directly provide the View layer to the user.

🚵 Worked Skills:

- Implement an API using MVC layered architecture.
- Use Docker for Python projects.
- Apply knowledge of Object Orientation in WEB development.
- Write tests for APIs to ensure endpoint implementation.
- Interact with a non-relational MongoDB database.
- Develop Server Side web pages.

<details>
    <summary><strong>Portuguese Description</strong></summary></br>

    Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Back-end (pela controller) fornecerá diretamente a camada View, para a pessoa usuária.

    🚵 Habilidades a trabalhadas:

    - Implementar uma API utilizando arquitetura em camadas MVC.
    - Utilizar o Docker para projetos Python.
    - Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
    - Escrever testes para APIs para garantir a implementação dos endpoints.
    - Interagir com um banco de dados não relacional MongoDB.
    - Desenvolver páginas web Server Side.

</details>

<br>

<details>
    <summary><strong>How to run</strong></summary></br>

    1. Clone this repository with:

        - `git clone git@github.com:NyPadilha/traduzo.git`
        - `cd  traduzo`

    Using Venv:

        1. Create the Virtual Environment:

            - `python3 -m venv .venv && source .venv/bin/activate`

        2. Install the dependencies:

            - `python3 -m pip install -r dev-requirements.txt`

    [Option A] Database and Flask with Docker:

        - `docker compose up translate`
        - `docker compose exec -it translate python3 src/run_seeds.py`

    [Option B]: Database with Docker and Flask with Venv:

        - `docker compose up -d mongodb`
        - `python3 src/run_seeds.py`
        - `python3 src/app.py`

    Test:

        `python3 -m pytest`

</details>

<br>

## What I Coded

- part of src/app.py
- src/controllers/translate_controller.py
- src/database/db.py
- src/models/language_model.py
- src/views/templates/index.html
- tests/models/history/test_history_model.py

## What Trybe Coded

- Basically everything else
