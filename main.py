from flask import Flask, render_template, redirect, url_for
from forms import BillingProviderForm, SubscriberInformationForm, ClaimForm

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
        return redirect(url_for('subscriber_information'))
    return render_template('billing_provider.html', form=form)

@app.route('/subscriber', methods=['GET', 'POST'])
def subscriber_information():
    form = SubscriberInformationForm()
    if form.validate_on_submit():
        # Redirect to the claim information form after successful submission
        return redirect(url_for('claim_information'))
    return render_template('subscriber_information.html', form=form)

# New route for claim information
@app.route('/claim_information', methods=['GET', 'POST'])
def claim_information():
    form = ClaimForm()
    if form.validate_on_submit():
        claim_id = form.claim_id.data
        claim_identifier_transmission = form.claim_identifier_transmission.data
        # Use claim_id and claim_identifier_transmission for further processing
        return f"Claim ID: {claim_id}, Claim Transmission Identifier: {claim_identifier_transmission}"
    return render_template('claim_information.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
