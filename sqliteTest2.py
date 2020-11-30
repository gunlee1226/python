import sqlite3
from sqlite3 import Error

# SQLite DB 연결
conn = sqlite3.connect("test.db")

# auto commit 할때
#conn = sqlite3.connect("test.db", isolation_level=None)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS table1 \
    (id integer PRIMARY KEY, name text, birthday text)")

cursor.execute("INSERT INTO table1 \
    VALUES(1, 'LEE', '1987-00-00')")

# 데이터 삽입 방법 1
cursor = conn.execute("SELECT * FROM table1")

# 데이터 삽입 방법 2
cursor.execute("INSERT INTO table1(id, name, birthday) \
    VALUES(?,?,?)", \
    (2, 'KIM', '1990-00-00'))

# 데이터 삽입 방법 2
test_tuple = (
    (3, 'PARK', '1991-00-00'),
    (4, 'CHOI', '1999-00-00'),
    (5, 'JUNG', '1989-00-00')
)
cursor.executemany("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", test_tuple)

cursor.execute("SELECT * FROM table1")
print(cursor.fetchall())


# Sqlite DB 연결 해제
conn.close()