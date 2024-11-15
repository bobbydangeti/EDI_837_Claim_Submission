from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField, HiddenField, DateField
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
    provider_identifier = StringField(
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






class SubscriberInformationForm(FlaskForm):
    # Subscriber Last Name (NM103, mandatory)
    subscriber_last_name = StringField(
        "Subscriber Last Name",
        validators=[DataRequired(), Length(max=50)]  # Mandatory field
    )

    # Subscriber First Name (NM104, mandatory)
    subscriber_first_name = StringField(
        "Subscriber First Name",
        validators=[DataRequired(), Length(max=50)]  # Mandatory field
    )

    # Subscriber Middle Name (NM105, optional)
    subscriber_middle_name = StringField(
        "Subscriber Middle Name",
        validators=[Optional(), Length(max=50)]  # Optional field
    )

    # Identification Code Qualifier (NM108, hidden field with default "MI")
    id_code_qualifier = HiddenField(
        "Identification Code Qualifier",
        default="MI"  # Automatically filled as "MI" and hidden
    )

    # Subscriber Identifier (NM109, mandatory)
    subscriber_identifier = IntegerField(
        "Subscriber Identifier",
        validators=[DataRequired(), Regexp(r'^\d+$', message="Subscriber Identifier must be numeric.")]  # Mandatory field
    )

    # Address Line 1 (N301, mandatory)
    address_line1 = StringField(
        "Address Line 1",
        validators=[DataRequired(), Length(max=100)]  # Mandatory field
    )

    # Address Line 2 (N302, optional)
    address_line2 = StringField(
        "Address Line 2",
        validators=[Optional(), Length(max=100)]  # Optional field
    )

    # City (N401, mandatory)
    city = StringField(
        "City",
        validators=[DataRequired(), Length(max=50)]  # Mandatory field
    )

    # State (N402, mandatory)
    state = StringField(
        "State",
        validators=[DataRequired(), Length(max=2)]  # Mandatory field
    )

    # ZIP Code (N403, mandatory)
    zip_code = StringField(
        "ZIP Code",
        validators=[
            DataRequired(),
            Regexp(r'^\d{5}(-\d{4})?$', message="Enter a valid ZIP Code.")  # Mandatory field with ZIP code pattern
        ]
    )

    # Country Code (N404, optional)
    country_code = StringField(
        "Country Code",
        validators=[DataRequired(), Regexp(r'^[A-Z]{2}$', message="Enter a valid 2-letter country code.")]  # Optional field
    )

    # Date of Birth (DMG02, mandatory)
    date_of_birth = DateField(
        "Date of Birth",
        validators=[DataRequired()],  # Mandatory field
        format='%Y%m%d'
    )

    # Gender (DMG03, mandatory)
    gender = SelectField(
        "Gender",
        choices=[('M', 'Male'), ('F', 'Female')],
        validators=[DataRequired()]  # Mandatory field
    )

    # Submit button
    submit = SubmitField("Next")
