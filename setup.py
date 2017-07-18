# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'pytest-ordering'
]

requires = [
    'dicttoxml',
    'geoalchemy2',
    'psycopg2',
    'pyramid',
    'pyramid_debugtoolbar',
    'PyYAML',
    'shapely',
    'simplejson',
    'SQLAlchemy',
    'sqlalchemy-utils',
    'transaction',
    'waitress',
    'zope.sqlalchemy',
    'jsonschema',
    'pyreproj',
    'lxml',
    'generateDS',
    'requests',
    'geolink_formatter'
]

setup(
    name='pyramid_oereb',
    version='1.0.0-alpha.2',
    description='pyramid_oereb, extension for pyramid web frame work to provide '
            'a basic server part for the oereb project',
    long_description='{readme}\n\n{changes}'.format(readme=README, changes=CHANGES),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    license='GNU General Public License',
    author='Clemens Rudert',
    author_email='clemens.rudert@bl.ch',
    url='https://github.com/camptocamp/pyramid_oereb',
    keywords='pyramid oereb',
    packages=find_packages(),
    package_data={'pyramid_oereb': [
        'standard/pyramid_oereb.yml.mako',
        'standard/logo_confederation.png',
        'standard/logo_oereb.png',
        'standard/logo_canton.png',
        'standard/templates/plr.py.mako',
        'tests/resources/*',
        'tests/resources/plr119/*'
    ]},
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pyramid_oereb:main'
        ],
        'console_scripts': [
            'create_standard_model = pyramid_oereb.standard.create_standard_models:create_standard_model',
            'create_standard_tables = pyramid_oereb.standard.create_tables:create_standard_tables',
            'create_theme_tables = pyramid_oereb.standard.create_tables:create_theme_tables',
            'create_standard_yaml = pyramid_oereb.standard.create_yaml:create_standard_yaml',
            'drop_standard_tables = pyramid_oereb.standard.drop_tables:drop_standard_tables',
        ],
    },
)
