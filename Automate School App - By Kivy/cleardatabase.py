import pymysql

con = pymysql.connect('localhost','database username','password','myschool')
cur = con.cursor()
cur.execute("SELECT * FROM demo;")
exist = cur.fetchall()
print(exist)
for i in range(100):
    cur.execute("DELETE FROM myschool.demo WHERE id=%s",(i))
    con.commit()
cur.execute("ALTER TABLE demo AUTO_INCREMENT =1")
con.close()
print('There is no data on database!')