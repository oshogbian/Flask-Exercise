from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store registered users
users = {}

# Hardcoded list of organizations
organizations = ["Organization A", "Organization B", "Organization C", "Organization D", "Organization E"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')

        # Backend validation
        if name and organization in organizations:
            users[name] = organization
            return redirect(url_for('registered'))
        else:
            return render_template('index.html', error="Please provide valid name and organization.")

    return render_template('index.html', active_page='home')

@app.route('/registered')
def registered():
    return render_template('registered.html', users=users, active_page='registered')

if __name__ == '__main__':
    app.run(debug=True)
