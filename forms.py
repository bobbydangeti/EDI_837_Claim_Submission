from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp

class BillingProviderForm(FlaskForm):
    entity_identifier = SelectField(
        "Entity Identifier Code",
        choices=[('85', 'Billing Provider'), ('87', 'Pay-to Provider')],
        validators=[DataRequired()]
    )
    entity_type_qualifier = SelectField(
        "Entity Type Qualifier",
        choices=[('1', 'Person'), ('2', 'Organization')],
        validators=[DataRequired()]
    )
    last_name = StringField(
        "Billing Provider Last Name/Organization Name",
        validators=[DataRequired(), Length(max=50)]
    )
    first_name = StringField(
        "Billing Provider First Name",
        validators=[Optional(), Length(max=50)]
    )
    middle_name = StringField(
        "Billing Provider Middle Name",
        validators=[Optional(), Length(max=50)]
    )
    id_code_qualifier = HiddenField(
        "Identification Code Qualifier",
        default="XX"
    )
    provider_identifier = IntegerField(
    "Billing Provider Identifier (NPI)",
    validators=[
        DataRequired(),
        Regexp(r'^\d{10}$', message="NPI must be exactly 10 digits.")
    ]
    )
    address_line1 = StringField(
        "Address Line 1",
        validators=[DataRequired(), Length(max=100)]
    )
    address_line2 = StringField("Address Line 2")
    city_name = StringField(
        "City Name",
        validators=[DataRequired()]
    )
    state = StringField(
        "State",
        validators=[DataRequired()]
    )
    postal_code = StringField(
        "Postal (ZIP) Code",
        validators=[DataRequired(), Regexp(r'^\d{5}(-\d{4})?$', message="Invalid ZIP Code")]
    )
    country_code = StringField(
        "Country Code",
        validators=[Optional(), Regexp(r'^[A-Z]{2}$', message="Invalid Country Code")]
    )
    reference_id_qualifier = SelectField(
        "Reference Identification Qualifier",
        choices=[('SY', 'SSN'), ('EI', 'Employer ID')],
        validators=[DataRequired()]
    )
    secondary_identifier = StringField(
        "Billing Provider Secondary Identifier",
        validators=[Optional(), Length(max=20)]
    )
    contact_function_code = SelectField(
        "Contact Function Code",
        choices=[('IC', 'Information Contact')],
        validators=[DataRequired()]
    )
    contact_name = StringField(
        "Billing Provider Contact Name",
        validators=[Optional(), Length(max=50)]
    )
    communication_number_qualifier = SelectField(
        "Communication Number Qualifier",
        choices=[('TE', 'Telephone')],
        validators=[DataRequired()]
    )
    communication_number = StringField(
        "Communication Number",
        validators=[DataRequired(), Regexp(r'^\d{10}$', message="Invalid phone number. Must be 10 digits.")]
    )
    submit = SubmitField("Next")
