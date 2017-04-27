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
        'pycodestyle==2.3.1',
        'pytest-cov==2.4.0',
        'pytest==3.0.6',
        'codeclimate-test-reporter==0.2.1',
    ],
    'packages': ['footyhints', 'tests'],
    'scripts': [],
    'name': 'footyhints'
}

setup(**config)
