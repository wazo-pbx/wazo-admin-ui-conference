# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import unittest
from mock import Mock, patch

from hamcrest import assert_that, contains, equal_to, has_entries, has_properties

from ..form import ConferenceForm
from ..view import ConferenceFormSchema


class TestSchemas(unittest.TestCase):

    @patch('wazo_admin_ui.plugins.conference.view.ConferenceForm')
    def test_conference_form_schema_load(self, conference_form):
        resources = {'conference': {'name': 'conference_1',
                                    'announce_join_leave': True,
                                    'extensions': [{'exten': '1234'}]}}

        ConferenceFormSchema().load(resources).data
        form = conference_form.call_args[1]

        expected_call = {'data': {'name': 'conference_1',
                                  'announce_join_leave': True},
                         'extension': '1234'}
        assert_that(form, equal_to(expected_call))

    def test_conference_form_schema_dump(self):
        # Do not use attribute name with Mock, it's reserved ...
        form = Mock(ConferenceForm,
                    music_on_hold=Mock(data='music'),
                    announce_join_leave=Mock(data=True),
                    extension=Mock(data='1234'))

        resources = ConferenceFormSchema().dump(form).data

        assert_that(resources, has_entries(conference=has_entries(music_on_hold='music',
                                                                  announce_join_leave=True),
                                           extension=has_entries(exten='1234',
                                                                 context='default')))

    def test_conference_form_schema_populate_form_error(self):
        form = Mock(ConferenceForm,
                    music_on_hold=Mock(errors=[]),
                    announce_join_leave=Mock(errors=[]),
                    extension=Mock(errors=[]))

        resources_errors = {'conference': {'music_on_hold': 'invalid length',
                                           'announce_join_leave': 'invalid type'},
                            'extension': {'exten': 'not in range'}}
        form = ConferenceFormSchema().populate_form_errors(form, resources_errors)

        assert_that(form, has_properties(
            music_on_hold=has_properties(errors=contains('invalid length')),
            announce_join_leave=has_properties(errors=contains('invalid type')),
            extension=has_properties(errors=contains('not in range')),
        ))
