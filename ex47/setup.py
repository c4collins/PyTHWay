try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Exercise 47 from Learn Python the Hard Way',
    'author': 'Connor Collins',
    'url': 'http://www.bittchinsdesign.ca/',
    'download_url': 'http://www.github.com/c4collins',
    'author_email': 'connorcollins@gmail.com',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)