from flask import Flask, render_template
from jinja2 import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

winners = [
    {'name': 'Albert Einstein', 'category':'Physics'},
    {'name': 'V.S. Naipaul', 'category':'Literature'},
    {'name': 'Dorothy Hodgkin', 'category':'Chemistry'}
]

@app.route('/demolist')
def demo_list():
    return render_template('testj2.html', heading="A little winners' list", winners=winners)

if __name__ == "__main__":
    app.run(port=8000, debug=True)