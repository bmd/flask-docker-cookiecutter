from flask_restful import Resource
from flask import url_for
import serializers
import models


class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            'resources': [
                {
                    'rel': 'self',
                    'href': url_for('home', _external=True)
                }
            ],
            'version': '0.0.1',
            'creators': [
                '{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>'
            ]
        }
