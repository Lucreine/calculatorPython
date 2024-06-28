from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'b=calculator.interface:main',
        ],
    },
)    