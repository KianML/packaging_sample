from setuptools import setup, find_packages

from sample_package_KianML import __version__

setup(
    name='sample_package_KianML',
    version=__version__,

    url='https://github.com/KianML/packaging_sample/src',
    author='Kianoosh Keshavarzian',
    author_email='kshvzn@gmail.com',
    test_suite='tests',
)
