from flask import Flask

app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return "<h1>Hallo</h1>"

@app.route('/25-01')
def kurs():
    return "<p>Hallo Kurs 25-01</p>"

@app.route('/about')
def about():
    return "Das ist die About-Seite über unser Projekt."

@app.route('/info')
def info():
    return "Das ist eine Info-Seite über Hunde-Salons"

if __name__ == "__main__":
    app.run(debug=True)