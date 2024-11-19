 
from flask import Flask, render_template, redirect, url_for
from forms import BillingProviderForm, SubscriberInformationForm, ClaimForm, ServiceLineForm
from Billing import insert_billing_provider
from Subscriber import insert_subscriber_information
from claim import insert_claim_information
from serviceline import insert_service_line

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Home route to redirect to billing_provider form
@app.route('/')
def home():
    return redirect(url_for('billing_provider'))

@app.route('/billing_provider', methods=['GET', 'POST'])
def billing_provider():
    form = BillingProviderForm()
    if form.validate_on_submit():
        # Map and insert form data into the database
        form_data = {field.name: field.data for field in form}
        insert_billing_provider(form_data)
        return redirect(url_for('subscriber_information'))
    return render_template('billing_provider.html', form=form)

@app.route('/subscriber', methods=['GET', 'POST'])
def subscriber_information():
    form = SubscriberInformationForm()
    if form.validate_on_submit():
        # Map and insert form data into the database
        form_data = {field.name: field.data for field in form}
        insert_subscriber_information(form_data)
        return redirect(url_for('claim_information'))
    return render_template('subscriber_information.html', form=form)

@app.route('/claim_information', methods=['GET', 'POST'])
def claim_information():
    form = ClaimForm()
    if form.validate_on_submit():
        # Map and insert form data into the database
        form_data = {field.name: field.data for field in form}
        insert_claim_information(form_data)
        return redirect(url_for('service_line'))
    return render_template('claim_information.html', form=form)

@app.route('/service_line', methods=['GET', 'POST'])
def service_line():
    form = ServiceLineForm()
    if form.validate_on_submit():
        # Map and insert form data into the database
        form_data = {field.name: field.data for field in form}
        insert_service_line(form_data)
        return "Service Line Submitted Successfully"
    return render_template('service_line.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
