from flask import Flask, render_template, redirect, url_for
from forms import BillingProviderForm, SubscriberInformationForm

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
        # Process subscriber form data
        pass
    return render_template('subscriber_information.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
