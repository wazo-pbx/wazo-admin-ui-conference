# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_destination_form, register_listing_url

from .service import ConferenceService
from .view import ConferenceView, ConferenceDestinationView
from .form import ConferenceDestinationForm

conference = create_blueprint('conference', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        ConferenceView.service = ConferenceService()
        ConferenceView.register(conference, route_base='/conferences')
        register_flaskview(conference, ConferenceView)

        ConferenceDestinationView.service = ConferenceService()
        ConferenceDestinationView.register(conference, route_base='/conference_destination')

        register_destination_form('conference', 'Conference', ConferenceDestinationForm)
        register_listing_url('conference', 'conference.ConferenceDestinationView:list_json')

        core.register_blueprint(conference)
