import pymysql

db= pymysql.connect(host='localhost',user='root',password='navercom123',
db = 'incheon_national',charset='utf8')

cur =db.cursor()

cur.execute("SELECT * FROM student")

rows =cur.fetchall()
print(rows)

db.close()