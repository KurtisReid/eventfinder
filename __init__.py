#!/usr/bin/env python


from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="Event Finder")

@app.route('/about/')
def helloWorld():
	return render_template("about.html", title="About Us")

if __name__ == '__main__':
    print( " * Your app is running on port 5000!")
    app.run(debug=True, port=5000)
