#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
    'validators',
    'packaging',
    'lxml'
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
    'pytest',
    'pytest-cov',
    'betamax',
    'betamax-serializers'
]

setup(
    name='changelogs',
    version='0.3.1',
    description="A changelog finder and parser.",
    long_description=readme + '\n\n' + history,
    author="Jannis Gebauer",
    author_email='jay@pyup.io',
    url='https://github.com/pyupio/changelogs',
    packages=[
        'changelogs',
    ],
    package_dir={'changelogs':
                 'changelogs'},
    entry_points={
        'console_scripts': [
            'changelogs=changelogs.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='changelogs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
