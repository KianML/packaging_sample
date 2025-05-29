from setuptools import setup, find_packages

from __init__ import __version__

setup(
    name='my_sample_package',
    version=__version__,

    url='https://github.com/kianData/Kian-Sample-Package',
    author='Kian',
    author_email='kshvzn@gmail.com',

    py_modules=['my_sample_package'],
)
