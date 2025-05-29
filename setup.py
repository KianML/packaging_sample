from setuptools import setup, find_packages

from my_sample_package import __version__

setup(
    name='my_sample_package',
    version=__version__,

    url='https://github.com/kianData/Kian_Sample_Package',
    author='Kian',
    author_email='kshvzn@gmail.com',
    test_suite='tests',
    py_modules=['my_sample_package'],
)
