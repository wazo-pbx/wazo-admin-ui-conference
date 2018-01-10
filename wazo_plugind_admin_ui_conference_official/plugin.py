# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_destination_form, register_listing_url
from wazo_admin_ui.helpers.funckey import register_funckey_destination_form

from .service import ConferenceService
from .view import ConferenceView, ConferenceDestinationView
from .form import ConferenceDestinationForm, ConferenceFuncKeyDestinationForm

conference = create_blueprint('conference', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        ConferenceView.service = ConferenceService()
        ConferenceView.register(conference, route_base='/conferences')
        register_flaskview(conference, ConferenceView)

        ConferenceDestinationView.service = ConferenceService()
        ConferenceDestinationView.register(conference, route_base='/conference_destination')

        register_funckey_destination_form('conference', l_('Conference'), ConferenceFuncKeyDestinationForm)
        register_destination_form('conference', l_('Conference'), ConferenceDestinationForm)
        register_listing_url('conference', 'conference.ConferenceDestinationView:list_json')

        core.register_blueprint(conference)
