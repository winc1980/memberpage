#http://localhost:5005/htmlFile

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_variable = "こんにちは、Flask!"
    return render_template('index.html', greeting=my_variable)
    

@app.route("/htmlFile")
def html_page():
    local_dict = {}
    local_dict["name"] = "鈴木風真"
    local_dict["team"] = "HPチーム"
    local_dict["uni"] = "早稲田大学"
    local_dict["intro"] = "HPチームリーダーです。"
    return render_template('profile_card.html',global_dict=local_dict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)