try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Connor Collins',
    'url': 'http://www.bittchinsdesign.ca/',
    'download_url': 'http://www.github.com/c4collins',
    'author_email': 'connorcollins@gmail.com',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)