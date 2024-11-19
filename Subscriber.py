from db_config import get_connection

def insert_subscriber_information(form_data):
    # Mapping of form fields to database columns
    subscriber_mapping = {
        'subscriber_last_name': 'Subscriber Last Name',
        'subscriber_first_name': 'Subscriber First Name',
        'subscriber_middle_name': 'Subscriber Middle Name',
        'id_code_qualifier': 'Identification Code Qualifier',
        'subscriber_identifier': 'Subscriber Identifier',
        'address_line1': 'Address Line 1',
        'address_line2': 'Address Line 2',
        'city': 'City',
        'state': 'State',
        'zip_code': 'ZIP Code',
        'country_code': 'Country Code',
        'date_of_birth': 'date_of_birth',
        'gender': 'Gender',
    }

    # Define the column order for the database
    database_columns = [
        'Subscriber Last Name', 'Subscriber First Name', 'Subscriber Middle Name',
        'Identification Code Qualifier', 'Subscriber Identifier', 'Address Line 1',
        'Address Line 2', 'City', 'State', 'ZIP Code', 'Country Code', 'date_of_birth',
        'Gender', 'claim id',
    ]

    # Map form data to match database columns
    ordered_data = [form_data.get(field, None) for field in subscriber_mapping.keys()]
    ordered_data.append(None)  # Add `None` for `claim id`

    try:
        # Connect to the database and insert data
        connection = get_connection()
        cursor = connection.cursor()

        # Prepare query
        columns_str = ", ".join(f"`{col}`" for col in database_columns)
        placeholders = ", ".join(["%s"] * len(database_columns))
        query = f"INSERT INTO `SubscriberInformationForm` ({columns_str}) VALUES ({placeholders})"

        print("Executing query:", query)  # Debugging
        print("With data:", ordered_data)  # Debugging

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
