# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdExtensionService
from wazo_admin_ui.helpers.confd import confd


class ConferenceService(BaseConfdExtensionService):

    resource_confd = 'conferences'

    def get_first_internal_context(self):
        result = confd.contexts.list(type='internal', limit=1, direction='asc', order='id')
        for context in result['items']:
            return context

    def get_context(self, context):
        result = confd.contexts.list(name=context)
        for context in result['items']:
            return context
