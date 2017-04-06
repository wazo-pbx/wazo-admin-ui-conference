# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import ConferenceForm


class ConferenceSchema(BaseSchema):

    class Meta:
        fields = extract_form_fields(ConferenceForm)


class ExtensionSchema(BaseSchema):
    context = fields.String(default='default')
    exten = fields.String(attribute='extension')


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'conference'

    conference = fields.Nested(ConferenceSchema)
    extension = fields.Nested(ExtensionSchema)


class ConferenceView(BaseView):

    form = ConferenceForm
    resource = l_('conference')
    schema = AggregatorSchema

    @classy_menu_item('.conferences', l_('Conferences'), order=1, icon="compress")
    def index(self):
        return super(ConferenceView, self).index()

    def _map_resources_to_form(self, resources):
        schema = self.schema()
        data = schema.load(resources).data
        main_exten = schema.get_main_exten(resources['conference'].get('extensions', {}))
        return self.form(data=data['conference'], extension=main_exten)


class ConferenceDestinationView(LoginRequiredView):

    def list_json(self):
        return self._list_json('id')

    def uuid_list_json(self):
        return self._list_json('uuid')

    def _list_json(self, field_id):
        params = extract_select2_params(request.args)
        conferences = self.service.list(**params)
        results = []
        for conference in conferences['items']:
            text = '{}'.format(conference['name'])
            results.append({'id': conference[field_id], 'text': text})

        return jsonify(build_select2_response(results, conferences['total'], params))
