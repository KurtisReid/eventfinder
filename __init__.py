from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title="Event Finder")

if __name__ == '__main__':
    print " * Your app is running on port 5000!"
    app.run(debug=True, port=5000)
