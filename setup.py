from setuptools import setup, find_packages

from main import __version__

setup(
    name='main',
    version=__version__,

    url='https://github.com/kianData/sample',
    author='Kian',
    author_email='kshvzn@gmail.com',
    test_suite='tests',
    py_modules=['main'],
)
