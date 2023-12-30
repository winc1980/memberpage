#http://localhost:5005/htmlFile

from flask import Flask, render_template, request
import mysql.connector
import base64

conn = mysql.connector.connect(
    host="memberpage-db-1",
    user="root",
    password="root",
    database="flask"
)


app = Flask(__name__)

cursor = conn.cursor()

global_dict = []

@app.route('/')
def index():
    #data_dict列
    data_dict = []
    data_dict_list = []
    global_dict = []
    cursor.execute("SELECT * FROM members_table")
    for row in cursor.fetchall():
        data_dict = {
            "name": row[0],
            "team": row[1],
            "role": row[2],
            "uni": row[3],
            "intro": row[4],
            "img": row[5] if row[5] is not None else "".encode()
        }
        data_dict_list.append(data_dict)
        print(data_dict)

    return render_template('test.html',global_dict_list=data_dict_list)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        team = request.form['team']
        post = request.form['post']
        university = request.form['university']
        introduction = request.form['introduction']
        img = request.files['img']
        if img:
            save_filename = "app/static/images/"+name+".jpg"
            upload_filename = name+".jpg"
            img.save(save_filename)

        # MySQLにデータを挿入するSQLクエリを実行
        cursor = conn.cursor()
        cursor.execute("INSERT INTO members_table (name, team, role, univ_faculty, self_intro, img) VALUES (%s, %s, %s, %s, %s, %s)", (name, team, post, university, introduction, upload_filename))
        conn.commit()
        cursor.close()

        return render_template('index.html',)

@app.route("/htmlFile")
def html_page():
    #data_dict列
    data_dict = []
    data_dict_list = []
    global_dict = []
    cursor.execute("SELECT * FROM members_table")
    for row in cursor.fetchall():
        data_dict = {
            "name": row[0],
            "team": row[1],
            "uni": row[2],
            "intro": row[3],
        }
        data_dict_list.append(data_dict)
        print(data_dict)

    return render_template('profile_card.html',global_dict_list=data_dict_list)
    
    

@app.route("/postForm")
def post_form():
    return render_template('profile_form.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

cursor.close()
conn.close()