'''
Created on 2020. 1. 17.

@author: gd7
dbex2.py : 화면에서 내용을 입력 받아 
'''
import sqlite3

dbpath = "test.sqlite"
con = sqlite3.connect(dbpath)
cur = con.cursor()
cur.executescript('''
drop table if exists usertable;
create table usertable (userid varchar(15) primary key, username varchar(20), email varchar(30), year integer);
''')

while True :
    data1 = input("사용자 ID=> ")
    if data1 == '' :
        break
    data2 = input("사용자 이름=>")
    data3 = input("이메일=>")
    data4 = input("출생 연도=>")
    sql = "insert into usertable values('"\
    + data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    con.commit()
#등록된 내용을 select로 조회하기
cur = con.cursor()
cur.execute("select * from usertable")
list = cur.fetchall() #모든 레코드 리턴
for row in list :
    print(row)
con.close()