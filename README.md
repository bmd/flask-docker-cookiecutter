# {{ cookiecutter.project_name }}

Author: {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

## Setup

```sh
$ pip install cookiecutter
$ cookiecutter gh:bmd/flask-docker-cookiecutter
$ cd {{ cookiecutter.app_name }}
$ docker-compose up --build
```

The application should now be running on localhost!