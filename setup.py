#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-urltree-field',
    version='0.1',
    author='Ralf Kostulski',
    author_email='webdeveloper@ralfkostulski.de',
    url='http://github.com/ralfzen',
    description='Creates a tree of URL-Nodes by crawling a website, which can be accessed in models by UrlTreeField.',
    #packages = ['inline_ordering',],
    packages=find_packages(),
    provides=['urltree',],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)