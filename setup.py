# -*- coding: utf-8 -*-
import sys
from setuptools import setup

if sys.version_info < (3, 0):

    long_description = "\n".join([
        open('README.md', 'r').read(),
    ])
else:
    long_description = "\n".join([
        open('README.md', 'r', encoding='utf-8').read(),
    ])

vsersion = '1.4.8'

setup(
    name='django-simpleui',
    version=vsersion,
    packages=['simpleui'],
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/newpanjing/simpleui',
    license='Apache License 2.0',
    author='panjing',
    long_description=long_description,
    author_email='newpanjing@icloud.com',
    description='django admin theme 后台模板',
    install_requires=['django'],
)
