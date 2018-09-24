from setuptools import *
from os import system


setup(
    author = 'xrust',
    name = 'rsatool',
    version = '0.4',
    scripts = ['bin/rsatool'],
    packages = find_packages()
)
