from setuptools import setup, find_packages


setup(
    name='spoonacular',
    version='1.0',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
