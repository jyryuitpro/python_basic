# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/Users/jyryu/PycharmProjects/python_basic/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, phone TEXT, website TEXT, regdate TEXT)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Ryu', 'tester@gmail.com', '010-xxxx-xxxx', 'tester.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Park', 'park@gmail.com', '010-yyyy-yyyy', 'park.com', nowDatetime,))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'lee@gmail.com', '010-zzzz-zzzz', 'lee.com', nowDatetime,),
    (4, 'Cho', 'cho@gmail.com', '010-0000-0000', 'cho.com', nowDatetime,),
    (5, 'Yoo', 'yoo@gmail.com', '010-0101-0101', 'yoo.com', nowDatetime,),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)
# conn.rollback()
# conn.commit()

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
# conn.close()