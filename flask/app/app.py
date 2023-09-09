#http://localhost:5005/htmlFile

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',)

# データベース接続
conn = mysql.connector.connect(
    host="memberpage-db-1",
    user="root",
    password="root",
    database="flask"
)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        team = request.form['team']
        post = request.form['post']
        university = request.form['university']
        introduction = request.form['introduction']

        # MySQLにデータを挿入するSQLクエリを実行
        cursor = conn.cursor()
        cursor.execute("INSERT INTO members_table (name, team, role, univ_faculty, self_intro) VALUES (%s, %s, %s, %s, %s)", (name, team, post, university, introduction))
        conn.commit()
        cursor.close()

        return render_template('index.html',)

@app.route("/htmlFile")
def html_page():
    local_dict = {}
    local_dict["name"] = "鈴木風真"
    local_dict["team"] = "HPチーム"
    local_dict["uni"] = "早稲田大学"
    local_dict["intro"] = "HPチームリーダーです。"
    return render_template('profile_card.html',global_dict=local_dict)

@app.route("/postForm")
def post_form():
    return render_template('profile_form.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)