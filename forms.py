from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, TextAreaField, HiddenField, DateField, SubmitField
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
    subscriber_identifier = StringField(
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

    date_of_birth = StringField(
        "Date of Birth",
        validators=[
            DataRequired(),
            Regexp(r'^\d{2}-\d{2}-\d{4}$', message="Date of Birth must be in DD-MM-YYYY format.")
        ]
    )
    # Gender (DMG03, mandatory)
    gender = SelectField(
        "Gender",
        choices=[('M', 'Male'), ('F', 'Female')],
        validators=[DataRequired()]  # Mandatory field
    )

    # Submit button
    submit = SubmitField("Next")


class ClaimForm(FlaskForm):
    # Claim Information
    claim_id = StringField("Claim ID", validators=[DataRequired(), Length(max=20)])
    claim_amount = DecimalField("Claim Amount", validators=[DataRequired(), NumberRange(min=0)], places=2)
    place_of_service_code = IntegerField("Place of Service Code", validators=[DataRequired(), NumberRange(min=1, max=99, message="Please enter a number between 1 and 99.")])
    claim_frequency_code = HiddenField("Claim Frequency Code", default="1", validators=[Optional(), Length(max=5)])
    
    provider_signature_indicator = HiddenField("Provider Signature Indicator", default="Y")  # Set the default value to "Y"
    assignment_of_benefits_indicator = HiddenField("Assignment of Benefits Indicator", default="Y")  # Set the default value to "Y"
    patient_signature_indicator = HiddenField("Patient Signature Indicator", default="Y")  # Set the default value to "Y"
    release_of_information_code = HiddenField("Release of Information Code", default="Y")  # Set the default value to "Y"

    # Dates and Service Information
    date_time_qualifier = HiddenField("Date/Time Qualifier", default="434")  # Set the default value to "434"
    date_format_qualifier = HiddenField("Date Format Qualifier", default="D8")  # Set the default value to "D8"
    date_of_service = DateField("Date of Service", validators=[DataRequired()], format='%Y-%m-%d')

    # Diagnosis Codes
    diagnosis_code_qualifier = HiddenField("Diagnosis Code Qualifier", default="ABK")  # Set the default value to "D8"
    diagnosis_code = StringField("Diagnosis Code", validators=[DataRequired(), Length(max=10)])
    additional_diagnosis_codes = StringField("Additional Diagnosis Codes", validators=[Optional(), Length(max=50)])

    # Reference Identifiers
    reference_id_qualifier = HiddenField("Reference Identification Qualifier", default="D9")  # Set the default value to "D8"
    claim_identifier_transmission = StringField("Claim Identifier for Transmission", validators=[DataRequired(), Length(max=20)])

    # Notes
    note_reference_code = HiddenField("Note Reference Code", default="ADD")  # Set the default value to "ADD"
    claim_note_text = TextAreaField("Claim Note Text", validators=[Optional(), Length(max=200)])

    # Amounts and Codes
    amount_qualifier_code = HiddenField("Amount Qualifier Code", default="F5")  # Set the default value to "F5"
    patient_amount_paid = DecimalField("Patient Amount Paid", validators=[Optional(), NumberRange(min=0)], places=2)
    report_type_code = HiddenField("Report Type Code", default="OB")  # Set the default value to "OB"
    report_transmission_code = HiddenField("Report Transmission Code", default="AA")  # Set the default value to "AA"

    # Patient Information
    patient_weight = DecimalField("Patient Weight", validators=[Optional(), NumberRange(min=0)], places=1)

    # Ambulance and Condition Information
    ambulance_transport_code = HiddenField("Ambulance Transport Code", default="N")  # Set the default value to "N"
    condition_indicator = SelectField(
        "Condition Indicator",
        choices=[("Y", "Yes"), ("N", "No")],
        validators=[Optional()],
        default="N"
    )
    condition_code = SelectField(
        "Condition Code",
        choices=[
            ("", "Select a Condition Code"),  # Placeholder option
            ("04", "Hysterectomy Condition"),
            ("01", "Employment Related"),
            ("02", "Auto Accident"),
            ("03", "Other Accident"),
            ("05", "Congenital Anomaly"),
            ("06", "Cosmetic Surgery"),
        ],
        validators=[Optional()],
        default=""
    )

    # Submit Button
    submit = SubmitField("Submit Claim")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Automatically populate claim_identifier_transmission with claim_id
        if self.claim_id.data:
            self.claim_identifier_transmission.data = self.claim_id.data
