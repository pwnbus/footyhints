try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from footyhints.version import version

config = {
    'description': 'A tool to determine if a soccer/football game is worth watching.',
    'author': 'Brandon Myers',
    'url': 'https://github.com/pwnbus/footyhints',
    'download_url': 'https://github.com/pwnbus/footyhints/archive/master.zip',
    'author_email': 'pwnbus@mozilla.com',
    'version': version,
    'install_requires': [
        'dj-database-url===2.1.0',
        'django-redis===5.3.0',
        'django-user-agents',
        'django===4.2.5',
        'mysqlclient===2.1.1',
        'pillow',
        'python-dateutil',
        'pyyaml',
        'requests',
        'youtube-search-python',
    ],
    'packages': ['web', 'footyhints'],
    'scripts': [],
    'name': 'footyhints'
}

setup(**config)
