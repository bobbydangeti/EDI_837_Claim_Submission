from db_config import get_connection

# Mapping form fields to database columns for ClaimForm
claim_mapping = {
    'claim_id': 'claim_id',
    'claim_amount': 'claim_amount',
    'place_of_service_code': 'place_of_service_code',
    'claim_frequency_code': 'claim_frequency_code',
    'provider_signature_indicator': 'provider_signature_indicator',
    'assignment_of_benefits_indicator': 'assignment_of_benefits_indicator',
    'patient_signature_indicator': 'patient_signature_indicator',
    'release_of_information_code': 'release_of_information_code',
    'date_time_qualifier': 'date_time_qualifier',
    'date_format_qualifier': 'date_format_qualifier',
    'date_of_service': 'date_of_service',
    'diagnosis_code_qualifier': 'diagnosis_code_qualifier',
    'diagnosis_code': 'diagnosis_code',
    'additional_diagnosis_codes': 'additional_diagnosis_codes',
    'reference_id_qualifier': 'reference_id_qualifier',
    'claim_identifier_transmission': 'claim_identifier_transmission',
    'note_reference_code': 'note_reference_code',
    'claim_note_text': 'claim_note_text',
    'amount_qualifier_code': 'amount_qualifier_code',
    'patient_amount_paid': 'patient_amount_paid',
    'report_type_code': 'report_type_code',
    'report_transmission_code': 'report_transmission_code',
    'patient_weight': 'patient_weight',
    'ambulance_transport_code': 'ambulance_transport_code',
    'condition_indicator': 'condition_indicator',
    'condition_code': 'condition_code'
}

def insert_claim_information(form_data):
    # Define the column order for the database
    database_columns = [
        'claim_id', 'claim_amount', 'place_of_service_code', 'claim_frequency_code',
        'provider_signature_indicator', 'assignment_of_benefits_indicator', 'patient_signature_indicator',
        'release_of_information_code', 'date_time_qualifier', 'date_format_qualifier', 'date_of_service',
        'diagnosis_code_qualifier', 'diagnosis_code', 'additional_diagnosis_codes', 'reference_id_qualifier',
        'claim_identifier_transmission', 'note_reference_code', 'claim_note_text', 'amount_qualifier_code',
        'patient_amount_paid', 'report_type_code', 'report_transmission_code', 'patient_weight',
        'ambulance_transport_code', 'condition_indicator', 'condition_code'
    ]

    # Reorder form data to match database column order
    ordered_data = [form_data.get(col, None) for col in claim_mapping.keys()]

    try:
        # Connect to the database and insert data
        connection = get_connection()
        cursor = connection.cursor()

        # Correct column names with backticks
        columns_str = ", ".join(f"`{col}`" for col in database_columns)
        placeholders = ", ".join(["%s"] * len(database_columns))
        query = f"INSERT INTO `ClaimForm` ({columns_str}) VALUES ({placeholders})"

        # Debugging: Print query and data
        print("Executing query:", query)
        print("With data:", ordered_data)

        cursor.execute(query, ordered_data)
        connection.commit()
    except Exception as e:
        print(f"Database error: {e}")
        raise e
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
