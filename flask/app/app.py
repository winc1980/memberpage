#http://localhost:5005/htmlFile

from flask import Flask, render_template
import mysql.connector

conn = mysql.connector.connect(
    host="memberpage-db-1",
    user="root",
    password="root",
    database="flask"
)

app = Flask(__name__)

cursor = conn.cursor()

@app.route('/')
def index():
    my_variable = "こんにちは、Flask!"
    return render_template('index.html', greeting=my_variable)
    

@app.route("/htmlFile")
def html_page():
    #data_dict列
    data_dict = []
    data_dict_list = []
    cursor.execute("SELECT * FROM profile")
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
    
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

cursor.close()
conn.close()