from flask import Flask, render_template, redirect, url_for
from forms import ServiceLineForm
from db_config import get_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Mapping form fields to database columns for ServiceLineForm
service_line_mapping = {
    'assigned_number': 'assigned_number',
    'procedure_code_qualifier': 'procedure_code_qualifier',
    'procedure_code': 'procedure_code',
    'line_item_charge_amount': 'line_item_charge_amount',
    'unit_or_basis_code': 'unit_or_basis_code',
    'service_unit_count': 'service_unit_count',
    'diagnosis_code_pointer1': 'diagnosis_code_pointer1',
    'diagnosis_code_pointer2': 'diagnosis_code_pointer2',
    'date_time_qualifier': 'date_time_qualifier',
    'date_format_qualifier': 'date_format_qualifier',
    'service_date': 'service_date',
    'reference_id_qualifier': 'reference_id_qualifier',
    'line_item_control_number': 'line_item_control_number',
    'amount_qualifier_code': 'amount_qualifier_code',
    'approved_amount': 'approved_amount',
    'file_information': 'file_information',
    'note_reference_code': 'note_reference_code',
    'service_line_note_text': 'service_line_note_text',
    'purchased_service_provider_id': 'purchased_service_provider_id',
    'purchased_service_charge_amount': 'purchased_service_charge_amount',
    'claim_id': 'claim_id'
}


@app.route('/')
def home():
    return redirect(url_for('service_line'))

@app.route('/service_line', methods=['GET', 'POST'])
def insert_service_line(form_data):
    form = ServiceLineForm()
    if form.validate_on_submit():
        # Map form data to database columns
        form_data = {
            service_line_mapping[field.name]: field.data
            for field in form if field.name in service_line_mapping
        }

        # Define the column order for the database
        database_columns = [
            'assigned_number', 'procedure_code_qualifier', 'procedure_code',
            'line_item_charge_amount', 'unit_or_basis_code', 'service_unit_count',
            'diagnosis_code_pointer1', 'diagnosis_code_pointer2', 'date_time_qualifier',
            'date_format_qualifier', 'service_date', 'reference_id_qualifier',
            'line_item_control_number', 'amount_qualifier_code', 'approved_amount',
            'file_information', 'note_reference_code', 'service_line_note_text',
            'purchased_service_provider_id', 'purchased_service_charge_amount', 'claim_id'
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
            query = f"INSERT INTO `ServiceLineForm` ({columns_str}) VALUES ({placeholders})"

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
        return "Service line information submitted successfully and data inserted into the database."

    return render_template('service_line.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
 
