# -*- copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import TextField
from wtforms.fields import BooleanField

from wtforms.validators import InputRequired
from wtforms.validators import Optional


class ConferenceForm(FlaskForm):
    name = TextField('Name', [InputRequired()])
    extension = TextField('Extension', [Optional()])
    announce_join_leave = BooleanField('Announce join leave', default=True)
    announce_only_user = BooleanField('Announce only user', default=True)
    announce_user_count = BooleanField('Announce user count', default=True)
    music_on_hold = TextField('Music On Hold')
    pin = TextField('PIN', [Optional()])
    admin_pin = TextField('Admin PIN', [Optional()])
    preprocess_subroutine = TextField('Subroutine')
    quiet_join_leave = BooleanField('Quiet join/leave', default=True)
    submit = SubmitField('Submit')
