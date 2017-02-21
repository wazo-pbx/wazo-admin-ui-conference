# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields, post_load, pre_dump

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema

from .form import ConferenceForm


class ConferenceSchema(BaseSchema):

    class Meta:
        additional = ('name',
                      'announce_join_leave',
                      'announce_user_count',
                      'announce_only_user',
                      'music_on_hold',
                      'preprocess_subroutine',
                      'quiet_join_leave')


class ExtensionSchema(BaseSchema):
    context = fields.String(default='default')
    exten = fields.String(attribute='extension')


class ConferenceFormSchema(BaseSchema):
    _main_resource = 'conference'

    conference = fields.Nested(ConferenceSchema)
    extension = fields.Nested(ExtensionSchema)

    @post_load(pass_original=True)
    def create_form(self, data, raw_data):
        main_exten = self.get_main_exten(raw_data['conference'].get('extensions', {}))
        return ConferenceForm(data=data['conference'], extension=main_exten)

    @pre_dump
    def add_envelope(self, data):
        return {'conference': data,
                'extension': data}


class ConferenceView(BaseView):

    form = ConferenceForm
    resource = 'conference'
    schema = ConferenceFormSchema
    templates = {'list': 'conferences.html',
                 'edit': 'view_conference.html'}

    @classy_menu_item('.conferences', 'Conferences', order=1, icon="compress")
    def index(self):
        return super(ConferenceView, self).index()
