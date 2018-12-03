#!/usr/bin/env python3

from setuptools import (
        setup,
        find_packages,
        )

VERSION = '0.0.1'

setup(
        name='cherry',
        packages=find_packages(),
        version=VERSION,
        description='PyTorch Reinforcement Learning Framework',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        author='Seb Arnold',
        author_email='smr.arnold@gmail.com',
        url = 'https://github.com/seba-1511/cherry',
        download_url = 'https://github.com/seba-1511/cherry/archive/' + str(VERSION) + '.zip',
        license='License :: OSI Approved :: Apache Software License',
        classifiers=[],
        scripts=[]
)