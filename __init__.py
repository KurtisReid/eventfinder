#!/usr/bin/env python

from flask import (Flask,
                   render_template,
                   url_for,
                   flash,
                   request,
                   redirect,
                   g,
                   session)

from makeForm import events, find_event

app = Flask(__name__)
app.secret_key = 'REDACTED'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['city'] = request.form.get('city')
        session['category'] = request.form.get('category')
        session['date'] = request.form.get('get-date')
        return redirect(url_for('results', city=session['city'], category=session['category'], date=session['date']))
    return render_template("index.html")

@app.route('/about/')
def helloWorld():
    return render_template("about.html", title="About Us")

@app.route('/results/<city>/<category>/<date>/')
def results(city, category, date):
    info = find_event(date, category, city)
    return render_template('results.html', info=info)

if __name__ == '__main__':
    print( " * Your app is running on port 5000!")
    app.run(debug=True, port=5000)
