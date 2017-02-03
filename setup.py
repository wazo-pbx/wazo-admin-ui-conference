#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_admin_ui_conference',
    version='0.1',

    description='Wazo Admin Conference',

    author='Sylvain Boily',
    author_email='sboily@wazo.community',

    url='https://github.com/sboily/wazo-admin-conference',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'wazo_admin_ui.plugins': [
            'conference = conference.plugin:Plugin',
        ]
    }
)

