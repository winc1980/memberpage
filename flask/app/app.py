#http://localhost:5005/htmlFile

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_variable = "Здравствуйте, Flask!"
    return render_template('index.html', greeting=my_variable)

@app.route("/htmlFile")
def html_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)