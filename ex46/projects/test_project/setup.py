try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'This project is showing that I know how to use the distutils as laid out in Learn Python the Hard Way, Exercise 46.',
    'author': 'Connor Collins',
    'url': 'http://www.bittchinsdesign.ca/',
    'download_url': 'http://www.github.com/c4collins',
    'author_email': 'connorcollins@gmail.com',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['test_project'],
    'scripts': [],
    'name': 'Test_Project'
}

setup(**config)