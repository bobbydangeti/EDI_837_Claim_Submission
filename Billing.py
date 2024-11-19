from flask import Flask, render_template, redirect, url_for
from forms import BillingProviderForm
from db_config import get_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Mapping form fields to database columns
field_mapping = {
    'entity_identifier': 'Entity Identifier Code',
    'entity_type_qualifier': 'Entity Type Qualifier',
    'last_name': 'Billing Provider Last Name/Organization Name',
    'first_name': 'Billing Provider First Name',
    'middle_name': 'Billing Provider Middle Name',
    'id_code_qualifier': 'id_code_qualifier',
    'provider_identifier': 'Billing Provider Identifier (NPI)',
    'address_line1': 'Address Line 1',
    'address_line2': 'Address Line 2',
    'city_name': 'City Name',
    'state': 'State',
    'postal_code': 'Postal (ZIP) Code',
    'country_code': 'Country Code',
    'reference_id_qualifier': 'Reference Identification Qualifier',
    'secondary_identifier': 'Billing Provider Secondary Identifier',
    'contact_function_code': 'Contact Function Code',
    'contact_name': 'Billing Provider Contact Name',
    'communication_number_qualifier': 'Communication Number Qualifier',
    'communication_number': 'Communication Number',
}

@app.route('/')
def home():
    return redirect(url_for('billing_provider'))

@app.route('/billing_provider', methods=['GET', 'POST'])
def insert_billing_provider(form_data):
    form = BillingProviderForm()
    if form.validate_on_submit():
        # Map form data to database columns
        form_data = {
            field_mapping[field.name]: field.data
            for field in form if field.name in field_mapping
        }

        # Define the column order for the database
        database_columns = [
            'Entity Identifier Code', 'Entity Type Qualifier', 'Billing Provider Last Name/Organization Name',
            'Billing Provider First Name', 'Billing Provider Middle Name', 'id_code_qualifier',
            'Billing Provider Identifier (NPI)', 'Address Line 1', 'Address Line 2', 'City Name', 'State',
            'Postal (ZIP) Code', 'Country Code', 'Reference Identification Qualifier',
            'Billing Provider Secondary Identifier', 'Contact Function Code', 'Billing Provider Contact Name',
            'Communication Number Qualifier', 'Communication Number'
        ]

        # Reorder form data to match database column order
        ordered_data = [form_data.get(col, None) for col in database_columns]

        try:
            # Connect to the database and insert data
            connection = get_connection()
            cursor = connection.cursor()

            # Correct column names with backticks
            columns_str = ", ".join(f"`{col}`" for col in database_columns)
            placeholders = ", ".join(["%s"] * len(database_columns))
            query = f"INSERT INTO `Billing_provider` (`claim id`, {columns_str}) VALUES (NULL, {placeholders})"

            # Debugging: Print query and data
            print("Executing query:", query)
            print("With data:", ordered_data)

            cursor.execute(query, ordered_data)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Database error: {e}")
            return f"Error inserting data into the database: {e}"

        # Redirect or show a success message
        return "Form submitted successfully and data inserted into the database."

    return render_template('billing_provider.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
