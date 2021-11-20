from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import InputRequired, ValidationError


class SubmitAddressForm(FlaskForm):
    name = StringField('address', [InputRequired()])
    submit = SubmitField('submit-button')


    def validate_name(form, field):
        if len(field.data) < 6 and len(field.data) > 64:
            raise ValidationError('invalid address')

