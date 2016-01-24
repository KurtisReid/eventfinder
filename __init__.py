#!/usr/bin/env python

from flask import Flask, render_template, url_for, flash, request
import forms

app = Flask(__name__)
app.secret_key = 'REDACTED'

@app.route('/', methods=['GET', 'POST'])
def index():
    city = 0
    category = 0
    '''
    form = forms.SearchForm()
    if form.validate_on_submit():
        flash("Searching for matching results", "success")
        city = form.city.data
        category = form.category.data
    '''
    print request.form.get('get-date')
    return render_template("index.html", title="Event Finder",
                                         #form = form,
                                         city=city,
                                         category=category)


@app.route('/about/')
def helloWorld():
	return render_template("about.html", title="About Us")

if __name__ == '__main__':
    print( " * Your app is running on port 5000!")
    app.run(debug=True, port=5000)
