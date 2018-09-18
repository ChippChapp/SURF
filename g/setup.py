#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='g',
    version='0.1.0',
    description="cookiecutterbased glofrim version",
    long_description=readme + '\n\n',
    author="Jannis Hoch",
    author_email='j.m.hoch@uu.nl',
    url='https://github.com/Utrecht University/g',
    packages=[
        'g',
    ],
    package_dir={'g':
                 'g'},
    include_package_data=True,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='g',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    install_requires=[],  # FIXME: add your package's dependencies to this list
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    }
)
