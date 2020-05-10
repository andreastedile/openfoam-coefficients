from setuptools import setup

coeffs = 'coeffs'

setup(
    name='coeffs',
    version='1.0',
    author='Andrea Stedile',
    author_email='andrea.stedile@studenti.unitn.it',
    packages=[coeffs],
    scripts=[coeffs + '/coeffs'],
    install_requires=['setuptools', 'tabulate']
)
