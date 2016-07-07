from os import getenv


class Config(object):
    """
    Base app configuration
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}:{port}/{database}'.format(
        user=getenv('MYSQL_USER'),
        host=getenv('MYSQL_HOST'),
        password=getenv('MYSQL_PASSWORD'),
        database=getenv('MYSQL_DATABASE'),
        port=getenv('MYSQL_PORT')
    )


class Dev(Config):
    """
    Development app configuration
    """
    SQLALCHEMY_ECHO = True
    DEBUG = True


class Prod(Config):
    """
    Production app configuration
    """
    pass
