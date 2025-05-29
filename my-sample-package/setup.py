from setuptools import setup

from __init__ import __version__

setup(
    name='my_sample_package',
    version=__version__,

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='Michael Kim',
    author_email='mkim0407@gmail.com',

    py_modules=['my_pip_package'],
)
