from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pycorset',
    version='1.0.0',
    description='Yet another Python starter',
    url="https://github.com/4lm/pycorset",
    author="Alexis Michaltsis",
    author_email="alexis@michaltsis.net",
    long_description=readme,
    license=license,
    install_requires=[
    'sphinx'
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'pycorset = pycorset.start:main'
        ]
    })
