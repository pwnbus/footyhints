from os import environ


version = 'v.dev'
if 'FOOTYHINTS_VERSION' in environ:
    version = environ.get('FOOTYHINTS_VERSION')
