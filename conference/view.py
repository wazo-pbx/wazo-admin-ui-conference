# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import ConferenceForm


class ConferenceView(BaseView):

    resource_name = 'conference'
    form = ConferenceForm
    resource = l_('conference')

    @classy_menu_item('.conferences', l_('Conferences'), order=1, icon="compress")
    def index(self):
        return super(ConferenceView, self).index()

    def _map_resources_to_form(self, resources):
        return self.form(data=resources['conference'])

    def _map_form_to_resources(self, form, form_id=None):
        conference = form.to_dict()
        resources = {'conference': conference,
                     'extension': conference['extensions'][0]}
        if form_id:
            resources['conference']['id'] = form_id
        return resources

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('conference', {}))
        form.extensions[0].populate_errors(resources.get('extension', {}))
        return form


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
