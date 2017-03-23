# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_wtf import FlaskForm
from wtforms.fields import (SubmitField,
                            TextField,
                            SelectField,
                            BooleanField)
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.destination import DestinationHiddenField


class ConferenceForm(FlaskForm):
    name = TextField(l_('Name'), [InputRequired()])
    extension = TextField(l_('Extension'))
    announce_join_leave = BooleanField(l_('Announce join leave'), default=True)
    announce_only_user = BooleanField(l_('Announce only user'), default=True)
    announce_user_count = BooleanField(l_('Announce user count'), default=True)
    music_on_hold = TextField(l_('Music On Hold'))
    pin = TextField(l_('PIN'))
    admin_pin = TextField(l_('Admin PIN'))
    preprocess_subroutine = TextField(l_('Subroutine'))
    quiet_join_leave = BooleanField(l_('Quiet join/leave'), default=True)
    submit = SubmitField()

class ConferenceDestinationForm(FlaskForm):
    setted_value_template = '{conference_name}'

    conference_id = SelectField('Conference', choices=[])
    conference_name = DestinationHiddenField()
