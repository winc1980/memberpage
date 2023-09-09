#http://localhost:5005/htmlFile

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_variable = "こんにちは、Flask!"
    return render_template('index.html', greeting=my_variable)

@app.route("/htmlFile")
def html_page():
    local_name = "鈴木"
    local_team = "HPチーム"
    local_uni = "早稲田大学"
    local_intro = "HPチームリーダーです。"
    return render_template('profile_card.html', name=local_name, team=local_team, uni=local_uni, intro=local_intro)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)