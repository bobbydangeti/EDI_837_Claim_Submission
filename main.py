from flask import Flask, render_template, redirect, url_for, flash
from forms import BillingProviderForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection with Flask-WTF

@app.route('/', methods=['GET', 'POST'])
def billing_provider():
    form = BillingProviderForm()
    if form.validate_on_submit():
        flash("Form submitted successfully!", "success")
        return redirect(url_for('success'))

    return render_template('billing_provider.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
