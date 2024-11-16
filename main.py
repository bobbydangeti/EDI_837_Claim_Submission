from flask import Flask, render_template, redirect, url_for
from forms import BillingProviderForm, SubscriberInformationForm, ClaimForm, ServiceLineForm

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

@app.route('/claim_information', methods=['GET', 'POST'])
def claim_information():
    form = ClaimForm()
    if form.validate_on_submit():
        print("Form Submitted Successfully")
        return redirect(url_for('service_line'))
    else:
        print(form.errors)  # This will show validation errors if any field fails validation
    return render_template('claim_information.html', form=form)

# New route for service line information
@app.route('/service_line', methods=['GET', 'POST'])
def service_line():
    form = ServiceLineForm()
    if form.validate_on_submit():
        # Process service line data here
        return "Service Line Submitted Successfully"
    return render_template('service_line.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

