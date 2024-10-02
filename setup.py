from setuptools import setup
setup(
    name = 'Cron-Parser',
    version = '0.1.0',
    packages = ['parser'],
    entry_points = {
        'console_scripts': [
            'parse = parser.main:main'
        ]
    })