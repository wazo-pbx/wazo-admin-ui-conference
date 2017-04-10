# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            FormField,
                            FieldList,
                            BooleanField)
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.destination import DestinationHiddenField
from wazo_admin_ui.helpers.form import BaseForm


class ExtensionForm(BaseForm):
    exten = StringField(l_('Extension'))
    context = StringField(default='default')


class ConferenceForm(BaseForm):
    name = StringField(l_('Name'), [InputRequired()])
    extensions = FieldList(FormField(ExtensionForm), min_entries=1)
    announce_join_leave = BooleanField(l_('Announce join leave'), default=True)
    announce_only_user = BooleanField(l_('Announce only user'), default=True)
    announce_user_count = BooleanField(l_('Announce user count'), default=True)
    music_on_hold = StringField(l_('Music On Hold'))
    pin = StringField(l_('PIN'))
    admin_pin = StringField(l_('Admin PIN'))
    preprocess_subroutine = StringField(l_('Subroutine'))
    quiet_join_leave = BooleanField(l_('Quiet join/leave'), default=True)
    submit = SubmitField()


class ConferenceDestinationForm(BaseForm):
    setted_value_template = u'{conference_name}'

    conference_id = SelectField('Conference', choices=[])
    conference_name = DestinationHiddenField()
