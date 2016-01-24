#!/usr/bin/env python

from flask import (Flask,
                   render_template,
                   url_for,
                   flash,
                   request,
                   g,
                   session)

app = Flask(__name__)
app.secret_key = 'REDACTED'

@app.route('/', methods=['GET', 'POST'])
def index():
    session['city'] = request.form.get('city')
    session['category'] = request.form.get('category')
    session['date'] = request.form.get('date')
    return render_template("index.html", title="Event Findr")

@app.route('/about/')
def helloWorld():
    return render_template("about.html", title="About Us")

@app.route('/results/')
    return render_template()

if __name__ == '__main__':
    print( " * Your app is running on port 5000!")
    app.run(debug=True, port=5000)
