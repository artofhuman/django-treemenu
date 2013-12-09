#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-treemenu',
    version='0.1',
    description='Another reusable app for organize tree menus on django site',
    author='Pupkov Semen',
    author_email='semen.pupvko@gmail.com',
    url='https://github.com/artofhuman/django-treemenu',
    include_package_data = True,
    zip_safe=False,
    install_requires=[
        'django-mptt>=0.6.0',
        'feincms==1.7.7'
    ],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'
    ]
)
