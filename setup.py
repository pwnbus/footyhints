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
        "Flask",
        'pycodestyle',
        'coverage==4.3.4',
        'pytest-cov',
        'pytest',
        'codeclimate-test-reporter',
        'mock',
    ],
    'packages': ['footyhints', 'tests'],
    'scripts': [],
    'name': 'footyhints'
}

setup(**config)
