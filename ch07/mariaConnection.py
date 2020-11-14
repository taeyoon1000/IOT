import pymysql

db= pymysql.connect(host='localhost',user='root',password='navercom123',
db = 'myDB',charset='utf8')

cur =db.cursor()

cur.execute("SELECT * FROM a")

rows =cur.fetchall()
print(rows)

db.close()