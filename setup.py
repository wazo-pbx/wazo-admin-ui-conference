#!/usr/bin/env python
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup
from setuptools.command.egg_info import egg_info as _egg_info
from babel.messages import frontend as babel


class egg_info(_egg_info):
    def run(self):
        self.run_command('compile_catalog')
        _egg_info.run(self)


setup(
    name='wazo_admin_ui_conference',
    version='0.1',

    description='Wazo Admin Conference',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),
    setup_requires=['Babel'],
    install_requires=['Babel'],
    include_package_data=True,
    zip_safe=False,

    cmdclass={'egg_info': egg_info,
              'compile_catalog': babel.compile_catalog,
              'extract_messages': babel.extract_messages,
              'init_catalog': babel.init_catalog,
              'update_catalog': babel.update_catalog},
    entry_points={
        'wazo_admin_ui.plugins': [
            'conference = wazo_plugind_admin_ui_conference_official.plugin:Plugin',
        ]
    }
)
