# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema

from .form import ConferenceForm


class ConferenceSchema(BaseSchema):

    class Meta:
        fields = ('name',
                  'announce_join_leave',
                  'announce_user_count',
                  'announce_only_user',
                  'music_on_hold',
                  'preprocess_subroutine',
                  'quiet_join_leave',
                  'pin',
                  'admin_pin')


class ExtensionSchema(BaseSchema):
    context = fields.String(default='default')
    exten = fields.String(attribute='extension')


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'conference'

    conference = fields.Nested(ConferenceSchema)
    extension = fields.Nested(ExtensionSchema)


class ConferenceView(BaseView):

    form = ConferenceForm
    resource = 'conference'
    schema = AggregatorSchema

    @classy_menu_item('.conferences', 'Conferences', order=1, icon="compress")
    def index(self):
        return super(ConferenceView, self).index()

    def _map_resources_to_form(self, resources):
        schema = self.schema()
        data = schema.load(resources).data
        main_exten = schema.get_main_exten(resources['conference'].get('extensions', {}))
        return self.form(data=data['conference'], extension=main_exten)
