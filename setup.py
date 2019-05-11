from setuptools import setup

setup(
    name = 'mytodo',
    version = '0.0.1',
    packages = ['mytodo'],
    entry_points = {
        'console_scripts': [
            'mytodo = mytodo.__main__:main'
        ]
    })