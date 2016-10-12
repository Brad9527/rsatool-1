from setuptools import *

setup(
    author = 'XRUST',
    name = 'rsatool',
    version = '0.1',
    install_requires = ['gmpy', 'libnum'],
    packages = ['rsatool'],
    scripts = ['bin/rsatool']
)


