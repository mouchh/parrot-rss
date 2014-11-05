try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Generate from plain websites RSS feeds filtered by your own choices and conditions',
    'author': 'Cyril Mouchel',
    'url': 'https://github.com/mouchh/parrot-rss',
    'download_url': 'https://github.com/mouchh/parrot-rss/archive/master.zip',
    'author_email': 'mouchel.cyril@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['parrot'],
    'scripts': [],
    'name': 'parrot-rss'
}

setup(**config)
