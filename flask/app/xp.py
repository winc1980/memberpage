import mysql.connector

# データベース接続
conn = mysql.connector.connect(
    host="127.0.0.1:3306",
    user="root",
    password="root",
    database="flask"
)

# カーソルの作成
cursor = conn.cursor()

# クエリの実行
cursor.execute("SELECT * FROM profile")

# 結果の取得
rows = cursor.fetchall()
for row in rows:
    print(row)

# リソースの解放
cursor.close()
conn.close()
